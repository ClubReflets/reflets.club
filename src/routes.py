from server import app
from flask import render_template, request, jsonify
from forms import ContactForm, AskPhotographForm, LoginForm

# ----------------------------------
# Home page (without authentication)
# ----------------------------------
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/photos')
def photos():
  return render_template('photos.html')

@app.route('/service', methods=['GET', 'POST'])
def service():
  if request.method == 'GET':
    form = AskPhotographForm()
    return render_template('service.html', form=form)
  # POST
  return jsonify(request.form)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
  if request.method == 'GET':
    form = ContactForm()
    return render_template('contact.html', form=form)
  # POST
  return jsonify(request.form)

# ----------------------------------
# Authentication
# ----------------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'GET':
    form = LoginForm()
    return render_template('login.html', form=form)
  # POST
  pass

# ----------------------------------
# Administration (with authentication)
# ----------------------------------
