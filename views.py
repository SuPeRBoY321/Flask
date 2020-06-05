from app import app
from flask import render_template
from flask import flash
from flask import url_for
from models import Post
from login import RegistrationForm
from login import LoginForm


@app.route("/")
def index():
	return render_template('default.html') 

@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created of {form.username.date}!', 'success')
		return redirect(url_for('index'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.date == form.password.date == 'password':
			flash('You have been loggen in', 'success')
			return redirect(url_for('index'))
		else:
			flash('Login unsucceseful.Please check username and password')
	return render_template('login.html', title='Login', form=form)