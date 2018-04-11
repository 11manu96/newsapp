from server import app
from flask import request

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    language = request.args['user']

    #if key doesn't exist, returns None
    return '''<h1>The language value is: {}</h1>'''.format(language)