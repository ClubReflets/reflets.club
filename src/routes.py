# Import Flask modules & others
from flask import render_template, request, jsonify, redirect, url_for
from flask_login import login_required, login_user, logout_user, current_user
# Import custom modules
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

  if request.method == 'POST' and form.validate_on_submit():
    email = request.form.get('email')
    password = request.form.get('password')
    user = User.query.filter_by(email=email.lower()).first()

    if user and user.check_password(password):
      login_user(user)
      # TODO: Validate the next action (url)
      #  https://flask-login.readthedocs.io/en/latest/#login-example
      #  http://flask.pocoo.org/snippets/63/
      return redirect(url_for('admin'))

    error = 'Email ou mot de passe invalide.'

  return render_template('login.html', form=form, error=error)


@app.route('/logout', methods=['POST'])
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
  return render_template('admin/index.html', user=current_user)