import os
import assets
from flask import Flask
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader

# Run and configure Flask server
app = Flask(__name__)
env = os.environ.get('FLASK_ENV', 'development')
print(env)
app.config.from_object('config.%sConfig' % env.capitalize())

# Set the Assets (css, js, etc.)
assets_env = Environment(app)
loader = PythonAssetsLoader(assets)
for name,bundle in loader.load_bundles().items():
  assets_env.register(name, bundle)

# Load the routes
import routes