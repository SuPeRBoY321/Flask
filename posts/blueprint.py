from flask import Blueprint
from flask import render_template
from flask import request 


posts = Blueprint("posts", __name__, template_folder = "templates")

@posts.route("/")
def index():
	return render_template("posts/index.html", posts=posts)

