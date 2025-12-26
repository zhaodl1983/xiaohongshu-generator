# RednoteGen - 小红书图文生成神器

一款基于 AI 的小红书风格图文卡片生成工具，让你的长文秒变爆款图文！

![AI生成示意图](https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800)

## 核心功能亮点

### 🤖 AI 智能分析
采用 Google Gemini AI 模型，自动分析文章结构，智能提取核心观点，生成 6-9 张精美图卡。AI 会根据内容复杂度自主决定最佳图片数量。

![智能分析](https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800)

### 🎨 9 种精美风格
- **小红书风格** - 渐变背景，现代感十足
- **苹果极简** - 简约大气，高级感满满
- **多巴胺** - 色彩鲜艳，活力四射
- **Capsule** - 暗黑科技，程序员最爱
- **知识胶囊** - 赛博朋克，未来感爆棚
- **Notion** - 效率风格，清爽干净
- **孟菲斯** - 几何图形，艺术气息
- **新中式** - 国潮风格，文化底蕴
- **拍立得** - 复古胶片，文艺范儿

![多种风格](https://images.unsplash.com/photo-1561070791-2526d30994b5?w=800)

### ✏️ 预览编辑模式
生成后可以：
- 修改标题、副标题、标签
- 编辑每张卡片的要点内容
- 单独重新生成不满意的卡片
- 切换风格无需重新调用 AI

### 📷 智能图片分配（新功能！）
支持 Markdown 格式输入，自动提取图片并智能分配：
- AI 根据内容相关度分配图片
- 自动跳过 GIF 格式
- 无法访问的图片静默跳过
- 支持手动添加/删除/替换图片

![图片功能](https://images.unsplash.com/photo-1611162617474-5b21e879e113?w=800)

## 技术架构

- **后端**: Python + Flask
- **AI**: Google Gemini API
- **渲染**: Jinja2 模板 + Playwright 截图
- **前端**: 原生 HTML/CSS/JS

## 使用场景

1. **自媒体运营** - 快速将文章转为小红书图文
2. **知识分享** - 制作精美的知识卡片
3. **产品介绍** - 生成产品特性展示图
4. **读书笔记** - 将读书心得可视化

![使用场景](https://images.unsplash.com/photo-1432888622747-4eb9a8efeb07?w=800)

## 快速开始

```bash
# 安装依赖
pip install -r requirements.txt
playwright install chromium

# 启动服务
python app.py
```

访问 http://localhost:5000 即可使用！

---

**RednoteGen** - 让内容创作更简单 ✨
