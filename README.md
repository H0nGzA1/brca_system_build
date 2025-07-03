# BRCA System Build

## 项目简介

本项目为 Django + Vue3 + Electron 的一体化桌面应用构建仓库，支持前后端分离、Electron 封装桌面端、自动化多平台打包（macOS/Windows/Linux）。

---

## 目录结构

```
├── brca_system/           # 主体源码（前端web、后端backend）
│   ├── backend/           # Django/DRF 后端源码
│   └── web/               # Vue3 前端源码
├── electron-app/          # Electron 封装与集成
│   ├── static/            # 前端构建产物（自动生成）
│   ├── backend_dist/      # 后端可执行文件（自动生成，多平台）
│   └── main.js            # Electron 主进程入口
├── .github/workflows/     # GitHub Actions CI 配置
├── build_backend.sh       # 后端打包脚本
├── build_frontend.sh      # 前端打包脚本
├── build_electron.sh      # Electron 打包脚本
├── build_all.sh           # 一键全量打包脚本
├── .gitignore             # Git 忽略文件
└── README.md              # 项目说明文档
```

---

## 本地开发与打包流程

### 1. 前端（Vue3）
```bash
cd brca_system/web
pnpm install
pnpm run dev           # 本地开发
pnpm run build:electron # 构建 Electron 用前端产物
```

### 2. 后端（Django/DRF）
```bash
cd brca_system/backend
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py runserver  # 本地开发
# 打包为可执行文件（需在目标平台执行）
../../build_backend.sh
```

### 3. Electron 封装
```bash
cd electron-app
npm install
npm run electron:dev   # 开发调试
npm run electron:build # 打包桌面应用
```

### 4. 一键全量打包
```bash
./build_all.sh
```

---

## GitHub Actions 多平台 PyInstaller 打包

- `.github/workflows/pyinstaller-build.yml` 自动在 macOS、Windows、Linux 上用 PyInstaller 打包后端可执行文件，并上传 artifact。
- Windows 下 pyinstaller 命令需写成一行，避免续行符报错。
- 产物可在 Actions 页面下载，用于 Electron 集成。

---

## 常见问题 FAQ

### 1. PyInstaller 跨平台打包
- 不能在 macOS 上打包 Windows 的 exe，需在各自平台分别打包。
- 推荐用 GitHub Actions 自动多平台打包。

### 2. CI/CD 依赖问题
- `mysqlclient` 需在 CI 安装系统依赖（如 `default-libmysqlclient-dev`、`brew install mysql`）。
- 见 workflow 示例。

### 3. .gitignore
- 已自动生成，忽略 node_modules、__pycache__、build/dist、虚拟环境、产物等。

### 4. Electron 启动后端路径
- Electron 打包后，后端可执行文件需放在 asar 包外部，路径用 `process.resourcesPath` 拼接。

---

## 贡献与联系方式

- 欢迎 issue、PR 反馈与贡献。
- 作者：H0nGzA1
- GitHub: [https://github.com/H0nGzA1/brca_system_build](https://github.com/H0nGzA1/brca_system_build) 