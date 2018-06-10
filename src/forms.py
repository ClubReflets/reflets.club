from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField, DateField, TimeField
from wtforms.validators import DataRequired, Email, URL


class ContactForm(FlaskForm):
  name = StringField(validators=[DataRequired()])
  email = EmailField(validators=[DataRequired(), Email()])
  message = TextAreaField(validators=[DataRequired()])


class AskPhotographForm(FlaskForm):
  name = StringField(validators=[DataRequired()])
  email = EmailField(validators=[DataRequired(), Email()])
  date = DateField(validators=[DataRequired()])
  time = TimeField(validators=[DataRequired()])
  description = TextAreaField(validators=[DataRequired()])
  link = StringField(validators=[URL()])


class LoginForm(FlaskForm):
  email = EmailField(validators=[DataRequired(), Email()])
  password = PasswordField(validators=[DataRequired()])

