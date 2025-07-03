#!/bin/bash
# 初始化并打包 Electron 应用
cd electron-app || exit 1

# 安装 Electron 和 electron-builder（如未安装）
if [ ! -d "node_modules/electron" ]; then
  npm install electron@^27.0.0 --save-dev || exit 1
fi
if [ ! -d "node_modules/electron-builder" ]; then
  npm install electron-builder@^24.0.0 --save-dev || exit 1
fi

# 创建 assets 目录（用于图标等资源）
mkdir -p assets

# 打包 macOS 和 Windows 应用
echo "开始打包 macOS 和 Windows 应用..."
npx electron-builder -mw || exit 1

cd -
echo "[Electron] macOS 和 Windows 打包完成。"
echo "输出文件位置: electron-app/dist/" 