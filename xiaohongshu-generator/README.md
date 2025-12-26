# RednoteGen - 小红书图文卡片生成器

> 基于 AI 的智能图文卡片生成工具，一键将长文转换为精美的小红书风格图卡

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## ✨ 特性

- 🤖 **AI 智能分析** - 自动分析内容结构，智能决定卡片数量（6-9张）
- 🎨 **9种精美风格** - 小红书、苹果极简、多巴胺、Capsule、科技、Notion、孟菲斯、新中式、拍立得
- 🔄 **秒速切换风格** - 生成一次，随意切换风格，无需重新调用 AI
- 📱 **完美适配** - 小红书标准 3:4 比例（1242x1660px）
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
| 苹果极简 | Bento Grid，高级感 | 干货知识、工具推荐 |
| 多巴胺 | 高饱和荧光色 | 创意灵感、潮流话题 |
| Capsule | 终端代码风格 | 技术教程、编程分享 |
| 知识胶囊 | 科技霓虹风 | AI、科技、硬核内容 |
| Notion | 效率笔记风格 | 学习笔记、待办清单 |
| 孟菲斯 | 复古波普风 | 年轻话题、潮流文化 |
| 新中式 | 国潮水墨风 | 传统文化、情感语录 |
| 拍立得 | 胶片复古风 | 生活记录、文艺内容 |

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
├── requirements.txt          # 依赖列表
├── DEPLOYMENT.md            # 部署文档
├── templates/               # Web 界面
│   └── index.html
├── template_*.html          # 9种风格模板
└── output/                  # 生成的图片
```

## 🚀 使用方式

### Web 界面（推荐）

1. 启动服务：`python app.py`
2. 访问 http://localhost:5000
3. 粘贴长文内容
4. 选择风格
5. 点击生成
6. 下载图片

### 命令行

```bash
# 编辑 input.txt 文件
echo "你的长文内容" > input.txt

# 运行生成
python main.py

# 查看输出
ls output/
```

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

### v1.0.0 (2025-12-15)
- ✨ 初始版本发布
- 🎨 支持 9 种图卡风格
- 🤖 AI 智能决定卡片数量
- 🔄 风格快速切换
- 🌐 Web 界面

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
