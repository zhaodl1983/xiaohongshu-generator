@echo off
chcp 65001 >nul
cls

echo ========================================
echo 🚀 RednoteGen - 小红书图文卡片生成器
echo ========================================
echo.

REM 检查 Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ 错误: 未找到 Python
    echo 请先安装 Python 3.9 或更高版本
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✓ Python 已安装

REM 检查配置文件
if not exist "config.py" (
    echo.
    echo ⚠️  未找到 config.py 配置文件
    echo.
    if exist "config.example.py" (
        echo 正在创建配置文件...
        copy config.example.py config.py >nul
        echo ✓ 已创建 config.py
        echo.
        echo ⚠️  请编辑 config.py 文件，填入你的 API Key
        echo    使用记事本打开: notepad config.py
        echo.
        echo 获取免费 Gemini API Key:
        echo    https://aistudio.google.com/app/apikey
        echo.
        pause
        exit /b 1
    ) else (
        echo ❌ 错误: 未找到 config.example.py
        pause
        exit /b 1
    )
)

echo ✓ 配置文件已就绪

REM 检查依赖
echo.
echo 检查依赖...

python -c "import flask" 2>nul
if errorlevel 1 (
    echo ⚠️  缺少依赖，正在安装...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo ❌ 依赖安装失败
        pause
        exit /b 1
    )
    echo ✓ 依赖安装完成
)

REM 检查 Playwright
python -c "from playwright.sync_api import sync_playwright" 2>nul
if errorlevel 1 (
    echo ⚠️  Playwright 未安装，正在安装...
    playwright install chromium
    if errorlevel 1 (
        echo ❌ Playwright 安装失败
        pause
        exit /b 1
    )
    echo ✓ Playwright 安装完成
)

echo ✓ 所有依赖已就绪

REM 创建输出目录
if not exist "output" mkdir output

REM 启动服务
echo.
echo ========================================
echo 🎉 启动 Web 服务...
echo ========================================
echo.
echo 访问地址: http://localhost:5000
echo.
echo 按 Ctrl+C 停止服务
echo.

python app.py

pause
