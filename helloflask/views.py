from flask import render_template
from helloflask import app

from version import version

@app.route('/')
def hello_flask():
    return render_template("index.html",version=version)


