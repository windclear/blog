from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for

from models import Todo


# 创建一个 蓝图对象 并且路由定义在蓝图对象中
# 然后在 flask 主代码中「注册蓝图」来使用
# 第一个参数是蓝图的名字，第二个参数是套路
main = Blueprint('todo', __name__)


@main.route('/')
def index():
    todo_list = Todo.query.all()
    return render_template('todo_index.html', todos=todo_list)


@main.route('/add', methods=['POST'])
def add():
    form = request.form
    t = Todo(form)
    t.save()
    return redirect(url_for('todo.index'))


@main.route('/delete/<int:todo_id>')
def delete(todo_id):
    t = Todo.query.get(todo_id)
    t.delete()
    return redirect(url_for('.index'))
