from app import app
from app import db
from app import bcrypt
from posts.blueprint import posts
from models import Post, User
import views


if __name__=="__main__":
	app.run(port=80)