print("=== BRCA Plugin Settings Loading ===")
print(f"Loading file: {__file__}")

from application import settings
import datetime
import os

# 版本信息 - 用于验证构建是否生效
BUILD_VERSION = "1.0.1"
BUILD_TIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
FILE_PATH = os.path.abspath(__file__)

print(f"BRCA Plugin loaded from: {FILE_PATH}")
print(f"Current working directory: {os.getcwd()}")
print(f"Python path: {sys.path}")

table_prefix = 'brca_'
# ================================================= #
# ***************** 插件配置区开始 *******************
# ================================================= #
# 路由配置
plugins_url_patterns = [
    {"re_path": r'', "include": "plugins.brca.urls"},
]
# app 配置
apps = ['plugins.brca']
# ================================================= #
# ******************* 插件配置区结束 *****************
# ================================================= #

middlewares = [
    # 'zhuoda_iot.middleware.CheckApiKeyMiddleware',
]

# ********** 注册app **********
settings.INSTALLED_APPS += [app for app in apps if app not in settings.INSTALLED_APPS]

# ********** 注册中间件 **********
settings.MIDDLEWARE += middlewares

# ********** 注册路由 **********
settings.PLUGINS_URL_PATTERNS += plugins_url_patterns

# 打印构建信息
print(f"=== BRCA Plugin Debug Info ===")
print(f"Version: {BUILD_VERSION}")
print(f"Build Time: {BUILD_TIME}")
print(f"File Path: {FILE_PATH}")
print(f"URL Patterns: {plugins_url_patterns}")
print(f"Apps: {apps}")
print(f"===============================")