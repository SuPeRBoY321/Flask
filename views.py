from app import app
from flask import render_template
from models import Post
from login import RegistrationForm
from login import LoginForm


@app.route("/")
def index():
	return render_template('base.html') 

@app.route("/register")
def register():
	form = RegistrationForm()
	return render_template('login.html', title='Login', form=form)