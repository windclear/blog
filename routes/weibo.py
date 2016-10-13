from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import abort

from models import Weibo
from models import User
from models import CommentWeibo
from .user import current_user

main = Blueprint('weibo', __name__)


@main.route('/')
def index():
    weibo_list = Weibo.query.all()
    c_list = CommentWeibo.query.all()
    return render_template('weibo/index.html', weibos=weibo_list, user=current_user(), User=User, comments=c_list)


@main.route('/add/', methods=['POST'])
def add():
    u = current_user()
    if u is not None:
        form = request.form
        w = Weibo(form)
        w.user_id = u.id
        w.save()
        return redirect(url_for('weibo.index'))
    else:
        abort(401)


@main.route('/add_comment/', methods=['POST'])
def add_comment():
    u = current_user()
    if u is not None:
        form = request.form
        c = CommentWeibo(form)
        c.user_id = u.id
        c.save()
        return redirect(url_for('weibo.index'))
    else:
        abort(401)
