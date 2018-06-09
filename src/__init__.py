import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader
from . import assets

# Run and configure Flask server
app = Flask(__name__)
env = os.environ.get('FLASK_ENV', 'development')
app.config.from_object('config.%sConfig' % env.capitalize())

# Database
db = SQLAlchemy(app)


# Set the Assets (css, js, etc.)
assets_env = Environment(app)
loader = PythonAssetsLoader(assets)
for name, bundle in loader.load_bundles().items():
  assets_env.register(name, bundle)


# Load the routes
from . import routes