# RednoteGen - 小红书图文卡片生成器

> 基于 AI 的智能图文卡片生成工具，一键将长文转换为精美的小红书风格图卡

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## ✨ 特性

- 🤖 **AI 智能分析** - 自动分析内容结构，智能决定卡片数量（6-9张）
- 😀 **Emoji 智能插入** - AI 自动在每个要点前添加相关 emoji，让内容更生动
- 🚫 **违禁词检测** - 内置敏感词库，发布前一键检测，高亮标红违规词
- 🎨 **10种精美风格** - 小红书、苹果极简、多巴胺、Capsule、科技、Notion、孟菲斯、新中式、拍立得、流光卡片
- 🔄 **秒速切换风格** - 生成一次，随意切换风格，无需重新调用 AI
- �  **智能图片分配** - 支持 Markdown 图片自动提取，AI 智能分配到相关卡片
- 🖼️ **统一图片尺寸** - 所有风格图片尺寸统一，布局美观一致
- 📐 **完美适配** - 小红书标准 3:4 比例（1242x1660px）
- 🌐 **现代化界面** - 简洁美观的 Web 操作界面
- 💾 **一键下载** - 支持单张或批量下载图片

## 🎬 快速开始

### 1. 安装依赖

```bash
pip install -r requirements.txt
playwright install chromium
```

### 2. 配置 API Key

```bash
# 复制配置示例
cp config.example.py config.py

# 编辑 config.py，填入你的 Gemini API Key
# 获取免费 API Key: https://aistudio.google.com/app/apikey
```

### 3. 启动服务

```bash
python app.py
```

访问 http://localhost:5000 开始使用！

## 📖 详细文档

查看 [DEPLOYMENT.md](DEPLOYMENT.md) 获取完整的部署和使用指南。

## 🎨 风格预览

| 风格 | 特点 | 适用场景 |
|------|------|----------|
| 小红书 | 紫粉渐变，经典风格 | 通用内容 |
| 苹果极简 | 纯黑白灰，高级感 | 干货知识、工具推荐 |
| 多巴胺 | 高饱和荧光色 | 创意灵感、潮流话题 |
| Capsule | 终端代码风格 | 技术教程、编程分享 |
| 知识胶囊 | 蓝紫渐变风 | AI、科技、硬核内容 |
| 备忘录 | 苹果 Notes 风格 | 学习笔记、待办清单 |
| 孟菲斯 | 复古波普风 | 年轻话题、潮流文化 |
| 新中式 | 国潮水墨风 | 传统文化、情感语录 |
| 拍立得 | 胶片复古风 | 生活记录、文艺内容 |
| 流光卡片 | 动态渐变光晕 | 科技产品、高端内容 |

## 🛠️ 技术栈

- **后端**: Python 3.9+, Flask
- **AI**: Google Gemini API
- **模板**: Jinja2
- **截图**: Playwright
- **前端**: HTML5, CSS3, JavaScript

## 📂 项目结构

```
xiaohongshu-generator/
├── app.py                    # Web 服务
├── main.py                   # 命令行工具
├── config.py                 # 配置文件（需自行创建）
├── config.example.py         # 配置示例
├── sensitive_words.py        # 敏感词库模块
├── requirements.txt          # 依赖列表
├── DEPLOYMENT.md            # 部署文档
├── CHANGELOG_UI.md          # UI更新日志
├── QUICKSTART.md            # 快速启动指南
├── templates/               # Web 界面
│   └── index.html
├── template_*.html          # 10种风格模板
└── output/                  # 生成的图片
```

## 🚀 使用方式

### Web 界面（推荐）

1. 启动服务：`python app.py`
2. 访问 http://localhost:5000
3. 粘贴长文内容（支持 Markdown 格式，自动提取图片）
4. 选择风格
5. 点击生成
6. 下载图片

### 命令行

```bash
# 编辑 input.txt 文件（支持 Markdown 格式）
echo "你的长文内容" > input.txt

# 运行生成
python main.py

# 查看输出
ls output/
```

### 图片功能

- **Markdown 图片支持**: 使用 `![描述](图片URL)` 语法，AI 会自动提取并智能分配图片
- **图片格式**: 支持 PNG、JPG、JPEG、WEBP（自动跳过 GIF）
- **智能分配**: AI 根据内容相关度将图片分配到对应卡片
- **统一尺寸**: 所有风格的图片高度统一，布局美观一致

## ⚙️ 配置说明

### API 选择

支持三种 API：

1. **Google Gemini**（推荐，免费）
   ```python
   GEMINI_API_KEY = "your-key"
   MODEL_NAME = "models/gemini-2.5-flash-lite"
   ```

2. **OpenAI**
   ```python
   OPENAI_BASE_URL = "https://api.openai.com/v1"
   OPENAI_API_KEY = "sk-..."
   MODEL_NAME = "gpt-4o"
   ```

3. **DeepSeek**
   ```python
   OPENAI_BASE_URL = "https://api.deepseek.com"
   OPENAI_API_KEY = "sk-..."
   MODEL_NAME = "deepseek-chat"
   ```

### 图片尺寸

```python
IMAGE_WIDTH = 1242   # 宽度
IMAGE_HEIGHT = 1660  # 高度（3:4 比例）
```

## 🐛 常见问题

### API 配额超限

**问题**: `429 You exceeded your current quota`

**解决**:
- 等待 24 小时配额重置
- 切换到 `gemini-2.5-flash-lite` 模型
- 查看配额: https://ai.dev/usage

### Playwright 安装失败

**解决**:
```bash
# 使用国内镜像
export PLAYWRIGHT_DOWNLOAD_HOST=https://npmmirror.com/mirrors/playwright/
playwright install chromium
```

### 端口被占用

**解决**:
```bash
# 修改 app.py 最后一行
app.run(debug=True, port=5001)  # 改为其他端口
```

更多问题查看 [DEPLOYMENT.md](DEPLOYMENT.md)

## 📝 更新日志

### v1.1.0 (2026-01-01)
- 🚫 新增违禁词检测功能：内置敏感词库（8大分类200+词汇），一键检测高亮显示
- 🎨 界面布局优化：左侧面板精简、风格选择横向排列自动换行
- 📐 输入框固定高度，生成按钮始终可见
- 🗂️ 风格选择和预览合并到同一卡片区域

### v1.0.3 (2025-12-31)
- 😀 新增 Emoji 智能插入功能：AI 自动在每个要点前添加相关 emoji，让内容更生动

### v1.0.2 (2025-12-31)
- 🎨 多巴胺风格封面背景色更换为翠绿色 (#00B894)
- 🔢 多巴胺风格页码优化为圆形黑底样式
- 🍎 苹果极简风格重新设计：纯黑白灰配色，编号列表布局
- 💊 知识胶囊风格重新设计：蓝紫渐变背景，白色内容卡片
- 📝 Notion 风格改为苹果备忘录风格：纯白背景，简洁线条
- 🔤 所有风格封面标题字号统一放大（110-130px）
- 🗑️ 修复生成新图卡时旧文件残留问题
- 🖼️ 小红书风格图片添加边框

### v1.0.1 (2025-12-26)
- 🖼️ 统一所有风格的图片尺寸和布局
- 🐛 修复拍立得风格标题显示问题
- ✨ 优化图片容器，确保视觉一致性

### v1.0.0 (2025-12-15)
- ✨ 初始版本发布
- 🎨 支持 9 种图卡风格
- 🤖 AI 智能决定卡片数量
- 🔄 风格快速切换
- 🌐 Web 界面
- 📷 Markdown 图片智能分配

## 📄 许可证

MIT License - 仅供学习和个人使用

## 🙏 致谢

- Google Gemini API
- Playwright
- Flask
- 所有开源贡献者

---

**如有问题或建议，欢迎提交 Issue！**

**祝你使用愉快！🎉**
