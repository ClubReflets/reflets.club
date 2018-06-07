import os
import assets

from flask import Flask, render_template
from flask_assets import Environment
from webassets.loaders import PythonLoader as PythonAssetsLoader
from forms import ContactForm

# Run and configure Flask server
app = Flask(__name__)
env = os.environ.get('FLASK_ENV', 'development')
print(env)
app.config.from_object('config.%sConfig' % env.capitalize())

# Assets
assets_env = Environment(app)
loader = PythonAssetsLoader(assets)
for name,bundle in loader.load_bundles().items():
  assets_env.register(name, bundle)

# Routes
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/photos')
def photos():
  return render_template('photos.html')

@app.route('/service')
def service():
  return render_template('service.html')

@app.route('/contact')
def contact():
  form = ContactForm()
  return render_template('contact.html', form=form)
