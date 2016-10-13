from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask import abort
import json

from models import Blog
from models import User
from models import CommentBlog
from .user import current_user

main = Blueprint('api', __name__)


@main.route('/comment/add', methods=['POST'])
def comment_add():
    u = current_user()
    print('comment_add', u.id, u.username)
    if u is not None:
        print('comment_add', u.id, u.username)
        form = request.form
        c = CommentBlog(form)
        c.user_id = u.id
        c.blog_id = int(form.get('blog_id', -1))
        c.save()
        d = {
            'id': c.id,
            'content': c.content,
            'created_time': c.created_time,
            'blog_id': c.blog_id,
            'user_id': c.user_id,
            'username': u.username,
        }
        return json.dumps(d, ensure_ascii=False)
        # return c.json()
    else:
        abort(401)
