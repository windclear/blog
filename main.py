from init import app

from routes.index import main as index_routes
from routes.todo import main as todo_routes
from routes.weibo import main as weibo_routes
from routes.blog import main as blog_routes
from routes.user import main as user_routes
from routes.api import main as api_routes
import errors


app.register_blueprint(index_routes, url_prefix='')
app.register_blueprint(todo_routes, url_prefix='/todo')
app.register_blueprint(weibo_routes, url_prefix='/weibo')
app.register_blueprint(user_routes, url_prefix='/user')
app.register_blueprint(blog_routes, url_prefix='/blog')
app.register_blueprint(api_routes, url_prefix='/api')


if __name__ == '__main__':
    app.run(debug=True, port=3000)
