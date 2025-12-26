#!/usr/bin/env python3
"""
小红书图文生成工具
读取长文 -> AI 总结为幻灯片 -> 渲染 HTML -> Playwright 截图
"""

import json
import os
import asyncio
from pathlib import Path

from jinja2 import Environment, FileSystemLoader
from playwright.async_api import async_playwright
import google.generativeai as genai

import config


def read_input_file(filepath: str = "input.txt") -> str:
    """读取输入的长文文件"""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def summarize_to_slides(content: str) -> dict:
    """调用 Gemini API 将长文总结为幻灯片格式的 JSON，AI 自主决定图片数量"""
    genai.configure(api_key=config.GEMINI_API_KEY)
    model = genai.GenerativeModel(config.MODEL_NAME)
    
    char_count = len(content)

    prompt = f"""你是一个专业的内容编辑，擅长将长文总结为小红书风格的图文内容。

请分析下面的长文，根据内容的信息量、结构和逻辑，自主决定需要多少张内容幻灯片（5-8张），输出严格的 JSON 格式：

{{
    "cover_title": "封面大标题（简短有力，10字以内）",
    "cover_subtitle": "封面副标题（一句话概括文章主旨）",
    "cover_tags": ["标签1", "标签2", "标签3"],
    "slides": [
        {{
            "title": "第1张幻灯片标题",
            "content": ["要点1", "要点2", "要点3", "要点4"]
        }},
        // ... 根据内容自主决定张数（5-8张内容页）
    ]
}}

图片数量决策原则：
- 分析文章的核心观点数量、信息密度、逻辑结构
- 如果内容简单、观点集中：5-6 张内容页即可
- 如果内容丰富、观点多元：7-8 张内容页更合适
- 确保每张幻灯片信息量充足，不要为了凑数而拆分
- 也不要为了压缩而丢失重要信息
- 最少 5 张内容页（总共 6 张含封面），最多 8 张内容页（总共 9 张含封面）

内容提炼要求：
1. 封面标题要吸引眼球，使用小红书风格的表达（10字以内）
2. 封面标签（cover_tags）要根据文章主题生成3-5个相关标签，每个标签3-6字
3. 每张幻灯片的 title 简洁有力（8字以内）
4. 每张幻灯片的 content 包含 3-5 个要点
5. 每个要点控制在 35 字以内，信息密度要高
6. 内容要有逻辑递进，从引入到总结

标签生成原则：
- 标签要与文章主题高度相关
- 使用小红书常见的标签风格（如：干货分享、实用技巧、新手必看等）
- 标签要简短有力，3-6个字
- 生成3-5个标签

内容提炼原则（重要）：
- 保留所有核心观点、关键数据、重要案例
- 不要丢失文章中的具体数字、百分比、时间节点等关键信息
- 如果文章有多个并列观点，每个观点都要体现
- 专有名词、产品名称、人名等必须保留
- 每张幻灯片信息量要充足，避免过度简化
- 优先保留"干货"内容，而非空泛的总结

文章字数：{char_count} 字
文章内容：
{content}

只输出 JSON，不要其他内容。"""

    response = model.generate_content(
        prompt,
        generation_config=genai.GenerationConfig(
            temperature=0.7,
            response_mime_type="application/json",
        ),
    )

    return json.loads(response.text)


def render_html(slides_data: dict, style: str = "xiaohongshu") -> str:
    """使用 Jinja2 渲染 HTML 模板"""
    # 根据风格选择模板
    template_map = {
        "xiaohongshu": "template.html",
        "apple": "template_apple.html",
        "dopamine": "template_dopamine.html",
        "capsule": "template_capsule.html",
        "tech": "template_tech.html",
        "notion": "template_notion.html",
        "memphis": "template_memphis.html",
        "chinese": "template_chinese.html",
        "polaroid": "template_polaroid.html",
    }
    
    template_file = template_map.get(style, "template.html")
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(template_file)
    return template.render(**slides_data)


async def capture_slides(html_content: str, output_dir: str = "output") -> list[str]:
    """使用 Playwright 截图每张卡片"""
    # 确保输出目录存在
    Path(output_dir).mkdir(exist_ok=True)

    # 创建临时 HTML 文件
    temp_html = Path("_temp_render.html")
    temp_html.write_text(html_content, encoding="utf-8")

    output_files = []

    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1600, "height": 2000},
            device_scale_factor=2,  # 高清截图
        )

        # 加载渲染后的 HTML
        await page.goto(f"file://{temp_html.absolute()}")
        await page.wait_for_load_state("networkidle")

        # 获取所有卡片元素并截图
        card_index = 1
        while True:
            card = page.locator(f"#card-{card_index}")
            if await card.count() == 0:
                break

            output_path = f"{output_dir}/slide_{card_index}.png"
            await card.screenshot(path=output_path)
            output_files.append(output_path)
            print(f"✅ 已生成: {output_path}")
            card_index += 1

        await browser.close()

    # 清理临时文件
    temp_html.unlink()

    return output_files


async def main():
    """主流程"""
    print("📖 读取输入文件...")
    content = read_input_file()
    char_count = len(content)
    print(f"   文章长度: {char_count} 字")

    print("\n🤖 调用 AI 分析内容并生成幻灯片...")
    print("   AI 将根据内容结构自主决定图片数量（6-9 张）")
    slides_data = summarize_to_slides(content)
    print(f"   封面标题: {slides_data['cover_title']}")
    print(f"   AI 决定生成: {len(slides_data['slides']) + 1} 张图片（1 封面 + {len(slides_data['slides'])} 内容页）")

    # 保存 JSON 结果
    with open("output/slides_data.json", "w", encoding="utf-8") as f:
        json.dump(slides_data, f, ensure_ascii=False, indent=2)
    print("\n💾 JSON 数据已保存到 output/slides_data.json")

    print("\n🎨 渲染 HTML 模板...")
    html_content = render_html(slides_data)

    print("\n📸 使用 Playwright 截图...")
    output_files = await capture_slides(html_content)

    print(f"\n🎉 完成！共生成 {len(output_files)} 张图片")
    print("   输出目录: output/")


if __name__ == "__main__":
    # 确保 output 目录存在
    Path("output").mkdir(exist_ok=True)
    asyncio.run(main())
