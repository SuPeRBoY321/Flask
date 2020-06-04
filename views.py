from app import app
from flask import render_template
from models import Post
from login import RegistrationForm
from login import LoginForm


@app.route("/")
def index():
	return render_template('default.html') 

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
	form = LoginForm()
	return render_template('Login.html', title='Register', form=form)