# 🌟 UV Installation Guide

## 💻 Python Installation (Step-by-Step for All OS)

---

### 💻 Windows

#### ✅ Step 1: Download Python
- Go to: [https://www.python.org/downloads/windows/](https://www.python.org/downloads/windows/)
- Click **"Download Python 3.x.x"** (latest version)

#### ✅ Step 2: Run Installer
- Double-click the `.exe` file  
- **Important:** Check ✅ **"Add Python to PATH"**
- Click **Install Now**

#### ✅ Step 3: Verify Installation
Open **Command Prompt** and type:
```bash
python --version
```

---

### 🍎 macOS

#### ✅ Option 1: Install via Homebrew
```bash
brew install uv
```

#### ✅ Option 2: Install via Script
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### ✅ Step 3: Verify
```bash
uv --version
```

---

### 🐧 Linux

#### ✅ Step 1: Install via Curl
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### ✅ Optional: If Needed, Add to PATH
```bash
export PATH="$HOME/.local/bin:$PATH"
```

#### ✅ Step 2: Verify
```bash
uv --version
```
