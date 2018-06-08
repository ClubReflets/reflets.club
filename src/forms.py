from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.fields.html5 import EmailField, DateField, TimeField
from wtforms.validators import DataRequired, Email, URL

class ContactForm(FlaskForm):
  name = StringField('Nom', validators=[DataRequired()])
  email = EmailField('Email', validators=[DataRequired(), Email()])
  message = TextAreaField('Message', validators=[DataRequired()])

class AskPhotographForm(FlaskForm):
  name = StringField('Nom', validators=[DataRequired()])
  email = EmailField('Email', validators=[DataRequired(), Email()])
  date = DateField('Date', validators=[DataRequired()])
  time = TimeField('Heure', validators=[DataRequired()])
  description = TextAreaField('Description', validators=[DataRequired()])
  link = StringField('Lien', validators=[URL()])