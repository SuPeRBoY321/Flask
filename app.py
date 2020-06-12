from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from posts.blueprint import posts
from flask_bcrypt import Bcrypt
from flask_login import LoginManager






app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
app.register_blueprint(posts, url_prefix="/blog")