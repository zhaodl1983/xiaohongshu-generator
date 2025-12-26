#!/bin/bash

# 清理脚本 - 打包前清理临时文件

echo "🧹 清理临时文件..."
echo ""

# 清理 Python 缓存
echo "清理 Python 缓存..."
find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null
find . -type f -name "*.pyc" -delete 2>/dev/null
find . -type f -name "*.pyo" -delete 2>/dev/null
find . -type f -name "*.pyd" -delete 2>/dev/null
echo "✓ Python 缓存已清理"

# 清理临时 HTML
echo "清理临时文件..."
rm -f _temp_render.html 2>/dev/null
echo "✓ 临时文件已清理"

# 清理输出目录（保留目录结构）
echo "清理输出目录..."
rm -f output/*.png 2>/dev/null
rm -f output/*.json 2>/dev/null
echo "✓ 输出目录已清理"

# 清理 macOS 系统文件
echo "清理系统文件..."
find . -name ".DS_Store" -delete 2>/dev/null
echo "✓ 系统文件已清理"

# 清理 IDE 配置
echo "清理 IDE 配置..."
rm -rf .vscode 2>/dev/null
rm -rf .idea 2>/dev/null
echo "✓ IDE 配置已清理"

echo ""
echo "✅ 清理完成！"
echo ""
echo "项目已准备好打包发布"
