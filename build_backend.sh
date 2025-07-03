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

# 使用 PyInstaller 打包，显式包含所有关键模块
pyinstaller main.py --onefile --name brca_backend \
  --hidden-import=application.settings \
  --hidden-import=application.celery \
  --hidden-import=application.asgi \
  --hidden-import=application.wsgi \
  --hidden-import=application.dispatch \
  --hidden-import=application.routing \
  --hidden-import=application.websocketConfig \
  --hidden-import=dvadmin \
  --hidden-import=dvadmin.utils \
  --hidden-import=dvadmin.utils.pagination \
  --hidden-import=dvadmin.utils.exception \
  --hidden-import=dvadmin.system \
  --hidden-import=plugins \
  --hidden-import=plugins.brca \
  --hidden-import=celery \
  --hidden-import=celery.fixups \
  --hidden-import=celery.app.trace \
  --hidden-import=celery.backends \
  --hidden-import=celery.loaders \
  --hidden-import=celery.fixups.django \
  --hidden-import=celery.loaders.app \
  --hidden-import=celery.loaders.default \
  --hidden-import=celery.loaders.base \
  --hidden-import=celery.loaders.settings \
  --hidden-import=celery.loaders.django \
  --hidden-import=dvadmin.utils.middleware \
  --hidden-import=django \
  --hidden-import=django.conf \
  --hidden-import=django.core.asgi \
  --hidden-import=django.core.wsgi \
  --hidden-import=django.core.handlers.asgi \
  --hidden-import=django.core.handlers.wsgi \
  --hidden-import=channels \
  --hidden-import=channels.layers \
  --hidden-import=channels_redis \
  --hidden-import=uvicorn \
  --hidden-import=gunicorn \
  --hidden-import=gevent \
  --hidden-import=pypinyin \
  --hidden-import=openpyxl \
  --hidden-import=whitenoise \
  --hidden-import=drf_yasg \
  --hidden-import=dvadmin3_celery \
  --hidden-import=django_cors_headers \
  --hidden-import=django_filter \
  --hidden-import=django_ranged_response \
  --hidden-import=django_restql \
  --hidden-import=django_simple_captcha \
  --hidden-import=django_timezone_field \
  --hidden-import=djangorestframework_simplejwt \
  --hidden-import=websockets \
  --hidden-import=user_agents \
  --hidden-import=tzlocal \
  --hidden-import=pyparsing \
  --hidden-import=ua_parser \
  --hidden-import=typing_extensions \
  --hidden-import=six \
  --hidden-import=requests \
  --hidden-import=Pillow \
  --hidden-import=mysqlclient \
  --hidden-import=whitenoise.middleware \
  || exit 1

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