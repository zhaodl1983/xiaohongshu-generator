# RednoteGen 本地部署文档

## 项目简介

RednoteGen 是一个基于 AI 的小红书图文卡片生成工具，支持将长文自动转换为精美的图文卡片。

**核心特性：**
- 🤖 AI 智能分析内容，自动决定卡片数量（6-9张）
- 🎨 9种精美风格：小红书、苹果极简、多巴胺、Capsule终端、知识胶囊、Notion、孟菲斯、新中式、拍立得
- 🔄 一键切换风格，无需重新生成
- 📱 完美适配小红书 3:4 比例（1242x1660px）
- 🌐 现代化 Web 界面，操作简单

---

## 系统要求

- **Python**: 3.9 或更高版本
- **操作系统**: macOS / Linux / Windows
- **浏览器**: Chrome / Firefox / Safari（推荐 Chrome）
- **网络**: 需要访问 Google Gemini API

---

## 快速开始

### 1. 克隆或下载项目

```bash
# 如果使用 Git
git clone <repository-url>
cd xiaohongshu-generator

# 或直接解压下载的 ZIP 文件
```

### 2. 安装依赖

```bash
# 安装 Python 依赖
pip install -r requirements.txt

# 或使用 pip3
pip3 install -r requirements.txt
```

**依赖说明：**
- `google-generativeai`: Google Gemini API SDK
- `flask`: Web 框架
- `jinja2`: HTML 模板引擎
- `playwright`: 浏览器自动化（用于截图）

**首次安装 Playwright 需要下载浏览器：**
```bash
playwright install chromium
```

### 3. 配置 API Key

#### 方式一：使用 Google Gemini（推荐）

1. 访问 [Google AI Studio](https://aistudio.google.com/app/apikey) 获取免费 API Key
2. 复制 `config.example.py` 为 `config.py`：
   ```bash
   cp config.example.py config.py
   ```
3. 编辑 `config.py`，替换 API Key：
   ```python
   GEMINI_API_KEY = "YOUR_GEMINI_API_KEY_HERE"  # 替换为你的真实 API Key
   MODEL_NAME = "models/gemini-2.5-flash-lite"
   ```

#### 方式二：使用 OpenAI 或 DeepSeek

编辑 `config.py`，取消注释对应配置：

```python
# OpenAI
OPENAI_BASE_URL = "https://api.openai.com/v1"
OPENAI_API_KEY = "sk-your-openai-key"
MODEL_NAME = "gpt-4o"

# 或 DeepSeek
OPENAI_BASE_URL = "https://api.deepseek.com"
OPENAI_API_KEY = "sk-your-deepseek-key"
MODEL_NAME = "deepseek-chat"
```

### 4. 启动服务

```bash
# 启动 Web 服务
python app.py

# 或使用 python3
python3 app.py
```

服务启动后，访问：**http://localhost:5000**

---

## 使用指南

### Web 界面使用

1. **输入内容**
   - 在左侧文本框粘贴你的长文（500-5000字）
   - AI 会自动分析内容结构和信息密度

2. **选择风格**
   - 点击风格卡片选择你喜欢的设计风格
   - 支持 9 种风格：
     - 小红书：经典紫粉渐变
     - 苹果极简：Bento Grid 布局
     - 多巴胺：高饱和荧光色
     - Capsule：终端代码风格
     - 知识胶囊：科技霓虹风
     - Notion：效率笔记风格
     - 孟菲斯：复古波普风
     - 新中式：国潮水墨风
     - 拍立得：胶片复古风

3. **生成图卡**
   - 点击 "Generate Slides" 按钮
   - 等待 AI 分析和生成（约 10-30 秒）
   - 生成后可在右侧预览所有卡片

4. **切换风格**
   - 生成后可直接点击其他风格卡片
   - 无需重新调用 AI，秒速切换

5. **下载图片**
   - 鼠标悬停在图片上，点击下载按钮
   - 图片保存在 `output/` 目录

### 命令行使用

如果你想通过命令行生成图卡：

```bash
# 1. 编辑 input.txt 文件，粘贴你的长文
nano input.txt

# 2. 运行生成脚本
python main.py

# 3. 查看生成的图片
ls output/
```

---

## 配置说明

### API 配额管理

**Gemini 免费层限制：**
- `gemini-2.5-flash`: 20次/天
- `gemini-2.5-flash-lite`: 更高配额（推荐）
- `gemini-2.0-flash`: 可能有独立配额

**如果遇到配额限制：**
1. 等待 24 小时配额重置
2. 切换到其他模型（修改 `config.py` 中的 `MODEL_NAME`）
3. 使用付费 API Key

### 图片尺寸调整

编辑 `config.py`：

```python
IMAGE_WIDTH = 1242   # 宽度（像素）
IMAGE_HEIGHT = 1660  # 高度（像素）
```

默认为小红书标准 3:4 比例。

### 自定义风格

如果你想添加新的风格：

1. 在项目根目录创建新模板文件：`template_mystyle.html`
2. 编辑 `main.py`，在 `template_map` 中添加映射：
   ```python
   template_map = {
       "mystyle": "template_mystyle.html",
       # ...
   }
   ```
3. 编辑 `templates/index.html`，添加风格选择卡片

---

## 常见问题

### 1. 安装 Playwright 失败

**问题：** `playwright install` 下载浏览器失败

**解决方案：**
```bash
# 使用国内镜像
export PLAYWRIGHT_DOWNLOAD_HOST=https://npmmirror.com/mirrors/playwright/
playwright install chromium
```

### 2. API Key 无效

**问题：** `401 Unauthorized` 或 `403 Forbidden`

**解决方案：**
- 检查 API Key 是否正确复制（无多余空格）
- 确认 API Key 是否已激活
- 访问 [Google AI Studio](https://aistudio.google.com/app/apikey) 重新生成

### 3. 配额超限

**问题：** `429 You exceeded your current quota`

**解决方案：**
- 等待 24 小时配额重置
- 切换到 `gemini-2.5-flash-lite` 模型
- 查看配额使用情况：https://ai.dev/usage

### 4. 生成速度慢

**问题：** 生成图卡需要很长时间

**原因：**
- AI 分析内容需要时间（10-20秒）
- Playwright 截图需要时间（5-10秒）

**优化建议：**
- 使用更快的模型（如 `gemini-2.0-flash`）
- 减少内容长度
- 确保网络连接稳定

### 5. 字体显示异常

**问题：** 中文字体显示为方块或乱码

**解决方案：**
```bash
# macOS
# 系统自带 PingFang SC，无需额外安装

# Linux
sudo apt-get install fonts-noto-cjk

# Windows
# 安装微软雅黑字体（系统自带）
```

### 6. 端口被占用

**问题：** `Address already in use: 5000`

**解决方案：**
```bash
# 方式一：杀死占用端口的进程
lsof -ti:5000 | xargs kill -9

# 方式二：修改端口
# 编辑 app.py 最后一行
app.run(debug=True, port=5001)  # 改为其他端口
```

---

## 项目结构

```
xiaohongshu-generator/
├── app.py                      # Flask Web 服务
├── main.py                     # 命令行生成脚本
├── config.py                   # 配置文件（需自行创建）
├── config.example.py           # 配置示例
├── requirements.txt            # Python 依赖
├── DEPLOYMENT.md              # 本文档
├── README.md                  # 项目说明
│
├── templates/                 # Web 界面模板
│   └── index.html            # 主页面
│
├── template.html              # 小红书风格模板
├── template_apple.html        # 苹果极简风格
├── template_dopamine.html     # 多巴胺风格
├── template_magazine.html     # Capsule 终端风格
├── template_tech.html         # 知识胶囊风格
├── template_notion.html       # Notion 风格
├── template_memphis.html      # 孟菲斯风格
├── template_chinese.html      # 新中式风格
├── template_polaroid.html     # 拍立得风格
│
├── output/                    # 生成的图片输出目录
└── input.txt                  # 命令行模式输入文件
```

---

## 技术栈

- **后端**: Python 3.9+, Flask
- **AI**: Google Gemini API
- **模板引擎**: Jinja2
- **截图**: Playwright (Chromium)
- **前端**: HTML5, CSS3, Vanilla JavaScript

---

## 性能优化建议

### 1. 使用更快的模型

```python
# config.py
MODEL_NAME = "models/gemini-2.0-flash"  # 更快但配额可能更低
```

### 2. 调整图片质量

编辑 `main.py` 中的截图参数：

```python
await card.screenshot(
    path=output_path,
    quality=80  # 降低质量以加快速度（默认 100）
)
```

### 3. 缓存机制

项目已实现风格切换缓存，生成一次后切换风格无需重新调用 AI。

---

## 安全建议

1. **不要提交 API Key 到 Git**
   - `config.py` 已添加到 `.gitignore`
   - 使用环境变量存储敏感信息

2. **生产环境部署**
   - 使用 `gunicorn` 或 `uwsgi` 替代 Flask 开发服务器
   - 配置 HTTPS
   - 添加访问限制和速率限制

3. **API Key 保护**
   ```bash
   # 使用环境变量
   export GEMINI_API_KEY="your-key-here"
   
   # 在 config.py 中读取
   import os
   GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
   ```

---

## 更新日志

### v1.0.0 (2025-12-15)
- ✨ 初始版本发布
- 🎨 支持 9 种图卡风格
- 🤖 AI 智能决定卡片数量
- 🔄 风格快速切换功能
- 🌐 Web 界面上线

---

## 许可证

本项目仅供学习和个人使用。

---

## 联系方式

如有问题或建议，欢迎提交 Issue。

---

## 致谢

- Google Gemini API
- Playwright 团队
- Flask 框架
- 所有开源贡献者

---

**祝你使用愉快！🎉**
