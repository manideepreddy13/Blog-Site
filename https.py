# return https response

from flask import Flask

app = Flask(__name__)


@app.route('/')
def begin():
    return 'https returned'
