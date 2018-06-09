import uuid


class BaseConfig(object):
  SECRET_KEY = str(uuid.uuid4())


class DevelopmentConfig(BaseConfig):
  SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/reflets.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = True
  SQLALCHEMY_ECHO = True


class ProductionConfig(BaseConfig):
  SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:@localhost/reflets'  # Change this
  pass
