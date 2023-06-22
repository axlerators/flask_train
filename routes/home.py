from flask import Blueprint
from flask import render_template

home_bp = Blueprint('home_bp', __name__)
@home_bp.route('/')
def home():
    name = "Bambang"
    return render_template('home.html', name=name)
