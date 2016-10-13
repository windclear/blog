from flask import Blueprint
from flask import render_template
from .user import current_user
from flask import request


main = Blueprint('index', __name__)


@main.route('/')
def index():
    return render_template('index.html', user=current_user())
