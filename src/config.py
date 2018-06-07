import uuid

class BaseConfig(object):
  SECRET_KEY = str(uuid.uuid4())

class DevelopmentConfig(BaseConfig):
  pass

class ProductionConfig(BaseConfig):
  pass
