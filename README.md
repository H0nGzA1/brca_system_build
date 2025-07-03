# BRCA 桌面端应用打包指南

本项目用于将 Django+DRF 后端和 Vue 前端打包成桌面端应用。

## 环境要求

### 系统要求
- macOS 10.14+ / Windows 10+ / Linux (Ubuntu 18.04+)
- Node.js 16+ 
- Python 3.8+
- Git

### 必需软件
1. **Node.js 和 npm**
   ```bash
   # macOS (使用 Homebrew)
   brew install node
   
   # Windows (下载安装包)
   # 访问 https://nodejs.org/ 下载安装
   
   # Linux
   curl -fsSL https://deb.nodesource.com/setup_16.x | sudo -E bash -
   sudo apt-get install -y nodejs
   ```

2. **Python 3.8+**
   ```bash
   # macOS
   brew install python@3.10
   
   # Windows
   # 访问 https://www.python.org/ 下载安装
   
   # Linux
   sudo apt-get install python3 python3-pip
   ```

3. **Git**
   ```bash
   # macOS
   brew install git
   
   # Windows
   # 访问 https://git-scm.com/ 下载安装
   
   # Linux
   sudo apt-get install git
   ```

## 项目结构

```
brca_system_build/           # 打包脚本目录
├── build_frontend.sh        # 前端构建脚本
├── build_backend.sh         # 后端打包脚本
├── build_electron.sh        # Electron 打包脚本
├── build_all.sh            # 一键打包脚本
└── electron-app/           # Electron 项目目录
    ├── main.js             # 主进程文件
    └── package.json        # 项目配置

../brca_system/             # 原项目目录
├── backend/                # Django 后端
└── web/                   # Vue 前端
```

## 快速开始

### 1. 克隆项目
```bash
# 确保你在 brca_system_build 目录下
cd /path/to/brca_system_build
```

### 2. 一键打包（推荐）
```bash
./build_all.sh
```

这个命令会自动执行以下步骤：
- 构建 Vue 前端
- 打包 Django 后端为可执行文件
- 打包 Electron 桌面应用

### 3. 分步打包（可选）

如果一键打包失败，可以分步执行：

#### 步骤 1：构建前端
```bash
./build_frontend.sh
```

#### 步骤 2：打包后端
```bash
./build_backend.sh
```

#### 步骤 3：打包桌面应用
```bash
./build_electron.sh
```

## 详细说明

### 前端构建
- 进入 `../brca_system/web` 目录
- 执行 `npm install` 安装依赖
- 执行 `npm run build` 构建静态文件
- 生成的文件位于 `../brca_system/web/dist`

### 后端打包
- 进入 `../brca_system/backend` 目录
- 安装 Python 依赖：`pip install -r requirements.txt`
- 安装 PyInstaller：`pip install pyinstaller`
- 打包为可执行文件：`pyinstaller main.py --onefile --name brca_backend`
- 生成的文件位于 `../brca_system/backend/dist/brca_backend`

### Electron 打包
- 初始化 Electron 项目（如果不存在）
- 安装 Electron 和 electron-builder
- 打包为桌面应用
- 生成的文件位于 `electron-app/dist`

## 输出文件

打包完成后，你会在以下位置找到生成的文件：

1. **前端静态文件**：`../brca_system/web/dist/`
2. **后端可执行文件**：`../brca_system/backend/dist/brca_backend`
3. **桌面应用**：`electron-app/dist/`

## 运行桌面应用

### 开发模式
```bash
cd electron-app
npm start
```

### 生产模式
直接运行 `electron-app/dist` 目录下的可执行文件。

## 常见问题

### 1. 权限问题
```bash
# 如果脚本无法执行，添加执行权限
chmod +x build_*.sh
```

### 2. Node.js 版本问题
```bash
# 检查 Node.js 版本
node --version
npm --version

# 如果版本过低，请升级到 16+
```

### 3. Python 环境问题
```bash
# 检查 Python 版本
python3 --version

# 如果使用虚拟环境，请先激活
source ../brca_system/backend/.venv/bin/activate  # macOS/Linux
# 或
../brca_system/backend/.venv/Scripts/activate     # Windows
```

### 4. 依赖安装失败
```bash
# 清理 npm 缓存
npm cache clean --force

# 清理 pip 缓存
pip cache purge

# 重新安装依赖
```

### 5. PyInstaller 打包失败
```bash
# 确保在正确的 Python 环境中
which python
which pip

# 检查是否安装了所有依赖
pip list | grep -E "(django|djangorestframework|uvicorn)"
```

## 自定义配置

### 修改应用信息
编辑 `electron-app/package.json`：
```json
{
  "name": "你的应用名称",
  "version": "1.0.0",
  "build": {
    "appId": "com.yourcompany.yourapp"
  }
}
```

### 修改窗口设置
编辑 `electron-app/main.js`：
```javascript
const win = new BrowserWindow({
  width: 1200,        // 窗口宽度
  height: 800,        // 窗口高度
  // 其他配置...
});
```

### 修改后端端口
编辑 `../brca_system/backend/main.py`：
```python
uvicorn.run("application.asgi:application", 
           reload=False, 
           host="0.0.0.0", 
           port=8000,  # 修改端口号
           workers=workers,
           log_config=LOGGING)
```

## 技术支持

如果遇到问题，请检查：
1. 环境版本是否符合要求
2. 网络连接是否正常
3. 磁盘空间是否充足
4. 权限是否足够

## 更新日志

- v1.0.0：初始版本，支持基本的桌面端打包功能 