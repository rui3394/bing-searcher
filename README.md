# Bing 自动搜索助手 (Windows 极简稳定版)

专为 Windows 系统打造的 Bing 自动化搜索脚本，支持**直接继承当前电脑 Edge 浏览器的登录状态**，单标签页循环复用搜索，避免打开大量无用标签页。

---

## 🌟 核心特性

1. **零调试端口，无视权限与路径问题**：
   - 不使用任何 9222 CDP 端口或底层参数，彻底告别 `--no-sandbox` 警告及端口无法连接的问题。
   - 完美兼容带有单引号等特殊字符的 Windows 用户名路径。
2. **100% 原生继承登录态**：
   - 直接启动系统的 Edge 浏览器，与日常使用完全一致，历史记录、微软账户、Cookies 全自动保留。
3. **单标签页循环复用**：
   - 通过系统剪贴板与地址栏快捷键，在同一个标签页中连续搜索 20 次，不产生多余垃圾标签页。
   - 搜完 20 次后，自动关闭该搜索标签页。
4. **高质量随机词库**：
   - 内置 300+ 条生活、科技、美食、旅游等日常搜索短语，每次随机抽取 20 条。

---

## 📁 文件结构

```text
bing_searcher/
├── search.py          # 核心 Python 脚本
├── words.txt          # 中文搜索词库 (300+ 真实日常关键词)
├── run.bat            # Windows 一键启动批处理文件
├── requirements.txt   # Python 依赖清单 (轻量 pyautogui, pyperclip)
└── README.md          # 说明文档
```

---

## 🚀 使用方法

### 方式一：双击一键运行（推荐）
在 Windows 电脑上直接**双击运行 `run.bat`**：
- 自动检测 Python；
- 自动安装轻量依赖库（`pyautogui`, `pyperclip`）；
- 自动调起 Edge 执行 20 次搜索并倒计时。

### 方式二：命令行运行
```cmd
pip install -r requirements.txt
python search.py
```

---

## ⚙️ 参数调整 (`search.py`)

打开 [`search.py`](file:///home/kali/projects/bing_searcher/search.py) 顶部配置区：
```python
SEARCH_COUNT = 20      # 搜索次数 (默认 20)
MIN_DELAY = 5.0        # 每次搜索后的最小等待秒数 (默认 5.0)
MAX_DELAY = 7.0        # 每次搜索后的最大等待秒数 (默认 7.0)
```
词库可随时在 [`words.txt`](file:///home/kali/projects/bing_searcher/words.txt) 中追加新词（每行一个）。
