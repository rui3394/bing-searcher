@echo off
chcp 65001 >nul
title Bing 自动搜索助手

echo ======================================================
echo           Bing 自动化搜索程序 (Windows 极简版)
echo ======================================================
echo.

:: 1. 检查是否安装了 Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [错误] 未检测到系统中的 Python！
    echo 请先前往 https://www.python.org/ 下载并安装 Python。
    echo 注意：安装时请务必勾选 "Add python.exe to PATH"！
    echo.
    pause
    exit /b
)

:: 2. 检查并自动安装轻量依赖库 (pyautogui, pyperclip)
python -c "import pyautogui, pyperclip" >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] 正在自动安装轻量快捷键依赖库 (pyautogui, pyperclip)...
    pip install -r requirements.txt
    if %errorlevel% neq 0 (
        echo [错误] 依赖安装失败，请检查网络连接。
        pause
        exit /b
    )
    echo [*] 依赖安装成功！
    echo.
)

:: 3. 运行搜索脚本
echo [*] 正在启动搜索任务...
echo.
python search.py

echo.
echo ======================================================
echo 任务已结束，按任意键退出窗口...
echo ======================================================
pause >nul
