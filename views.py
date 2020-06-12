from app import app
from app import db
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
		hashed_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user=User(username=form.username.date, email=form.email.date, password=hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('You account has been created! You are now able to log in', 'success')
		return redirect(url_for('login'))
	return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		if form.email.date == form.password.date == 'password':
			flash('You have been loggen in', 'success')
			return redirect(url_for('index'))
		else:
			flash('Login unsucceseful.Please check username and password', 'danger')
	return render_template('login.html', title='Login', form=form)