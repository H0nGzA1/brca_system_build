#!/bin/bash
bash build_frontend.sh || exit 1
bash build_backend.sh || exit 1
bash build_electron.sh || exit 1
echo "[全部] 桌面端一键打包完成！" 