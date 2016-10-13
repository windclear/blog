from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import abort
import time
from models import Blog
from models import User
from models import CommentBlog
from .user import current_user

main = Blueprint('blog', __name__)


# 首页显示所有blog
@main.route('/')
def index():
    u = current_user()
    bs = Blog.query.all()[::-1]
    return render_template('blog/index.html', user=u, blogs=bs, User=User, time=time)


# 用户主页, 显示当前用户所有blog
@main.route('/<user_id>')
def user_index(user_id):
    u = User.query.get(user_id)
    c_user = current_user()
    if u is not None:
        bs = u.blogs()[::-1]
        return render_template('user_index.html', user=c_user, username=u.username, blogs=bs, User=User, time=time)
    else:
        abort(401)


# 显示一篇blog
@main.route('/blogs/<blog_id>', methods=['GET'])
def blog_view(blog_id):
    u = current_user()
    b = Blog.query.get(blog_id)
    cs = CommentBlog.query.filter_by(blog_id=b.id).all()
    return render_template('blog_view.html', user=u, blog=b, comments=cs, User=User, time=time)


# 单独的新建blog页面
@main.route('/add', methods=['GET'])
def add():
    u = current_user()
    return render_template('blog_add.html', user=u)


# 提交blog
@main.route('/submit', methods=['POST'])
def submit():
    u = current_user()
    if u is not None:
        form = request.form
        b = Blog(form)
        b.user_id = u.id
        b.save()
        return redirect(url_for('.user_index', user_id=u.id))
    else:
        abort(401)
