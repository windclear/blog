from flask import render_template

from init import app


@app.errorhandler(404)
def error404(e):
    return render_template('404.html')
