#!/bin/bash
# 构建 Vue 前端
cd ../brca_system/web || exit 1
pnpm install || exit 1
pnpm run build:electron || exit 1
rm -rf ../../brca_system_build/electron-app/static
cp -r dist ../../brca_system_build/electron-app/static
cd -
echo "[前端] 构建完成。" 