import os
# Import Flask modules
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment
from flask_login import LoginManager
from webassets.loaders import PythonLoader as PythonAssetsLoader

# Import custom modules
from . import assets

# Run and configure Flask server
app = Flask(__name__)
env = os.environ.get('FLASK_ENV', 'development')
app.config.from_object('config.%sConfig' % env.capitalize())

# Database
db = SQLAlchemy(app)
from .models import User

# Set the Assets (css, js, etc.)
assets_env = Environment(app)
loader = PythonAssetsLoader(assets)
for name, bundle in loader.load_bundles().items():
  assets_env.register(name, bundle)

# Load the routes
from . import routes

# Configure Flask-Security for authentication
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return 'Access denied.'

