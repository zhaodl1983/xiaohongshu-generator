#!/bin/bash

# RednoteGen 启动脚本

echo "🚀 RednoteGen - 小红书图文卡片生成器"
echo "======================================"
echo ""

# 检查 Python 版本
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未找到 Python 3"
    echo "请先安装 Python 3.9 或更高版本"
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2 | cut -d'.' -f1,2)
echo "✓ Python 版本: $PYTHON_VERSION"

# 检查配置文件
if [ ! -f "config.py" ]; then
    echo ""
    echo "⚠️  未找到 config.py 配置文件"
    echo ""
    if [ -f "config.example.py" ]; then
        echo "正在创建配置文件..."
        cp config.example.py config.py
        echo "✓ 已创建 config.py"
        echo ""
        echo "⚠️  请编辑 config.py 文件，填入你的 API Key："
        echo "   nano config.py"
        echo ""
        echo "获取免费 Gemini API Key:"
        echo "   https://aistudio.google.com/app/apikey"
        echo ""
        exit 1
    else
        echo "❌ 错误: 未找到 config.example.py"
        exit 1
    fi
fi

echo "✓ 配置文件已就绪"

# 检查依赖
echo ""
echo "检查依赖..."

if ! python3 -c "import flask" 2>/dev/null; then
    echo "⚠️  缺少依赖，正在安装..."
    pip3 install -r requirements.txt
    
    if [ $? -ne 0 ]; then
        echo "❌ 依赖安装失败"
        exit 1
    fi
    
    echo "✓ 依赖安装完成"
fi

# 检查 Playwright
if ! python3 -c "from playwright.sync_api import sync_playwright" 2>/dev/null; then
    echo "⚠️  Playwright 未安装，正在安装..."
    playwright install chromium
    
    if [ $? -ne 0 ]; then
        echo "❌ Playwright 安装失败"
        exit 1
    fi
    
    echo "✓ Playwright 安装完成"
fi

echo "✓ 所有依赖已就绪"

# 创建输出目录
mkdir -p output

# 启动服务
echo ""
echo "======================================"
echo "🎉 启动 Web 服务..."
echo "======================================"
echo ""
echo "访问地址: http://localhost:5000"
echo ""
echo "按 Ctrl+C 停止服务"
echo ""

python3 app.py
