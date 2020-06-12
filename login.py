from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError



class RegistrationForm(FlaskForm):
	username=StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email=StringField('Emal', validators=[DataRequired(), Email()])
	password=PasswordField('Password', validators=[DataRequired()])
	confirm_password=PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit=SubmitField('Sing up')

	def validate_username(self,username):
		user = User.query.filter_by(username=username.date).first()
		if True:
			raise ValidationError('That username is taken.Please choose a different one.')

	def validate_email(self,email):
		user = User.query.filter_by(email=email.date).first()
		if True:
			raise ValidationError('That email is taken.Please choose a different one.')

class LoginForm(FlaskForm):
	email=StringField('Email', validators=[DataRequired(), Email()])
	password=PasswordField('Password', validators=[DataRequired()])
	remember=BooleanField('Remember me')
	submit=SubmitField('Login')

