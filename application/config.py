class BaseConfig:
    pass

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = "kjsdhakjhdkhdkjahkdj-devel"
    PORT=3000

class ProductionConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = 'dsdkahdshdksjdkahdasdjsahkdhsahd-production'

class TestingConfig(BaseConfig):
    TESTING = True
    SECRET_KEY = 'dsdkahdshdksjdkahdasdjsahkdhsahd-production'

