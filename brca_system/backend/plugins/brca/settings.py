from application import settings

table_prefix = 'brca_'
# ================================================= #
# ***************** 插件配置区开始 *******************
# ================================================= #
# 路由配置

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