from app import app
from posts.blueprint import posts
from app import db
import views


if __name__=="__main__":
	app.run()