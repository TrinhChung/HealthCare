from flask import Response,render_template, send_from_directory, Blueprint,current_app
import os

home_bp = Blueprint("home", __name__)

@home_bp.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html")