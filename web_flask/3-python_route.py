#!/usr/bin/python3
""" Script that starts a flask app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Home():
    """ function for route /
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def Hbnb():
    """ function route for /hbnb
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def PrintText(text):
    """ function for route /c/<text>
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def PrintText_2(text="is_cool"):
    """ Function for route /python/text
    """
    return "Python {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
