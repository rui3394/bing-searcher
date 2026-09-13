# -*- coding: utf-8 -*-
"""
Bing 自动搜索助手 (极简稳定版)
- 零底层配置与调试端口依赖，100% 继承本机 Edge 登录态
- 单标签页复用 (Ctrl+L -> Ctrl+V -> Enter)，搜完自动关闭 (Ctrl+W)
"""

import os
import time
import random
import subprocess
from urllib.parse import quote
from pathlib import Path

try:
    import pyautogui
    import pyperclip
except ImportError:
    pyautogui = None
    pyperclip = None

# ==================== 配置区 ====================
SEARCH_COUNT = 25           # 搜索总次数 (设为25次以确保拿满积分)
MIN_DELAY = 7.0             # 每次搜索后的最小等待秒数 (防冷却被吞分)
MAX_DELAY = 9.0             # 每次搜索后的最大等待秒数 (防风控识别)
# ================================================

def find_edge():
    """自动获取本机 Edge 安装路径"""
    for p in [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        os.path.expandvars(r"%LOCALAPPDATA%\Microsoft\Edge\Application\msedge.exe"),
    ]:
        if os.path.exists(p):
            return p
    return "msedge"

def load_words(count=25):
    """读取词库并随机抽取关键词"""
    word_file = Path(__file__).parent / "words.txt"
    if word_file.exists():
        with open(word_file, "r", encoding="utf-8") as f:
            words = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    else:
        words = ["今日热点新闻", "天气预报", "健康养生知识", "经典电影推荐", "家常菜做法"]
    return random.sample(words, min(count, len(words)))

def activate_edge():
    """确保 Edge 处于前台激活状态"""
    try:
        import ctypes
        hwnd = ctypes.windll.user32.FindWindowW("Chrome_WidgetWin_1", None)
        if hwnd:
            ctypes.windll.user32.ShowWindow(hwnd, 9)
            ctypes.windll.user32.SetForegroundWindow(hwnd)
    except Exception:
        pass

def main():
    if pyautogui is None or pyperclip is None:
        print("[错误] 缺少必要依赖库，请运行: pip install -r requirements.txt")
        return

    pyautogui.FAILSAFE = False
    words = load_words(SEARCH_COUNT)
    edge_path = find_edge()

    print("=" * 55)
    print(f"[*] 开始执行: 共 {len(words)} 次搜索，间隔 {MIN_DELAY}~{MAX_DELAY} 秒")
    print(f"[*] 使用浏览器: {edge_path}")
    print("=" * 55)

    # 1. 启动 Edge 并打开第 1 个搜索词 (继承本机登录态)
    first_url = f"https://cn.bing.com/search?q={quote(words[0])}&form=CALWHP"
    subprocess.Popen([edge_path, first_url])
    time.sleep(4.5)  # 等待浏览器初次加载

    # 2. 循环搜索 (单标签页复用)
    for idx, word in enumerate(words, 1):
        if idx > 1:
            url = f"https://cn.bing.com/search?q={quote(word)}&form=CALWHP"
            pyperclip.copy(url)
            activate_edge()
            pyautogui.hotkey('ctrl', 'l')
            time.sleep(0.2)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(0.2)
            pyautogui.press('enter')

        delay = random.uniform(MIN_DELAY, MAX_DELAY)
        print(f"[{idx:02d}/{len(words)}] 搜索: {word} | 等待 {delay:.1f}s")
        time.sleep(delay)

    # 3. 搜索结束，自动关闭标签页
    print("\n" + "=" * 55)
    print("🎉 全部搜索已完成！正在关闭标签页...")
    activate_edge()
    time.sleep(0.5)
    pyautogui.hotkey('ctrl', 'w')
    print("[*] 任务圆满结束！")
    print("=" * 55)

if __name__ == "__main__":
    main()
