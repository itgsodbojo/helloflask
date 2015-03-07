from helloflask import app

from version import version

@app.route('/')
def hello_flask():
    return 'Hello Flask version: %s!' % version


