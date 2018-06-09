from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
from . import app
from .models import User
from .forms import ContactForm, AskPhotographForm, LoginForm


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
  form = LoginForm()
  error = None

  if request.method == 'POST' and form.validate():
    user_email = request.form.get('email')
    user = User.query.filter_by(email=user_email.lower()).first()
    # TODO: Continue (handle password)
    if user:
      if login_user(user):
        return 'Good to login'
    error = 'Email ou mot de passe invalide.'

  return render_template('login.html', form=form, error=error)


@app.route('/logout', methods=['DELETE'])
@login_required
def logout():
  logout_user()
  return redirect(url_for('index'))


# ----------------------------------
# Administration (with authentication)
# ----------------------------------
@app.route('/admin', methods=['GET'])
@login_required
def admin():
  return 'Admin page'