#!/bin/bash
# 打包 Django/DRF 后端
cd ../brca_system/backend || exit 1

# 激活 uv 虚拟环境
source .venv/bin/activate || exit 1

# 使用 uv 安装依赖（如果使用 uv）
if command -v uv &> /dev/null; then
    uv pip install pyinstaller || exit 1
else
    # 回退到 pip
    pip install pyinstaller || exit 1
fi

# 清理旧的 build、dist 目录
rm -rf build dist __pycache__

# 使用 PyInstaller 通过 spec 文件打包
pyinstaller brca_backend.spec || exit 1

cd -

# 判断平台
PLATFORM=$(uname)
if [[ "$PLATFORM" == "Darwin" ]]; then
    OUTDIR="mac"
    OUTFILE="brca_backend"
elif [[ "$PLATFORM" == "Linux" ]]; then
    OUTDIR="linux"
    OUTFILE="brca_backend"
elif [[ "$PLATFORM" == "MINGW"* || "$PLATFORM" == "MSYS"* || "$PLATFORM" == "CYGWIN"* ]]; then
    OUTDIR="win"
    OUTFILE="brca_backend.exe"
else
    echo "Unknown platform: $PLATFORM"
    exit 1
fi

mkdir -p electron-app/backend_dist/$OUTDIR
cp ../brca_system/backend/dist/$OUTFILE electron-app/backend_dist/$OUTDIR/$OUTFILE

echo "[后端] PyInstaller 打包完成并已复制到 electron-app/backend_dist/$OUTDIR。"