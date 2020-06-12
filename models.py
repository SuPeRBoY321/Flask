from app import db
from datetime import datetime
import re
import sys  
from sqlalchemy import Column, ForeignKey, Integer, String  
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import relationship  
from sqlalchemy import create_engine  

def slugify(s):
	pattern = r'[^\w+]'
	return re.sub(pattern,'-', s)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	username = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(20), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)



	def __repr__(self):
		return f"User('{self.username}', '{self.email}')"

class Post(db.Model):	
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(140), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user_id'), nullable=False)

	def __repr__(self):
		return f"User('{self.title}', '{self.date_posted}', )"	
	
	def __init__(self, *args, **kwargs):
		super(Post, self).__init__(*args,**kwargs)
		self.generate_slug()

	def generate_slug(self):
		if self.title: 
			self.slug = slugify(self.title)


