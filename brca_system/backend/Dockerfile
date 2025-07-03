# 使用Python 3.10作为基础镜像
FROM python:3.10-slim as builder

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY requirements.txt .

# 安装Python依赖
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt

# 第二阶段：运行环境
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# 安装系统依赖
RUN apt-get update && apt-get install -y --no-install-recommends \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# 从builder阶段复制wheels
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .

# 安装Python依赖
RUN pip install --no-cache /wheels/*

# 复制项目文件
COPY . .

# 创建必要的目录
RUN mkdir -p /app/logs /app/media

# 设置权限
RUN chmod +x /app/manage.py

# 暴露端口
EXPOSE 8000

# 启动命令
CMD ["gunicorn", "application.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "4", "--timeout", "120"] 