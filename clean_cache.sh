#!/bin/bash
# 清理缓存目录脚本

echo "=== 清理缓存目录 ==="

# 1. 清理 PyInstaller 缓存
echo "1. 清理 PyInstaller 缓存..."
cd brca_system/backend
rm -rf build dist __pycache__ .pytest_cache
rm -rf .PyInstaller
rm -rf *.spec.bak
rm -rf .cache

# 2. 清理系统临时目录
echo "2. 清理系统临时目录..."
rm -rf /tmp/_MEI* 2>/dev/null || true
rm -rf /var/folders/*/T/_MEI* 2>/dev/null || true

cd ..
echo "=== 缓存清理完成 ==="
echo "现在可以提交代码到 GitHub 进行打包了" 