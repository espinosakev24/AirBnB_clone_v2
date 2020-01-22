#!/user/bin/python3
""" Script that starts flask app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Home():
    """ Function of route / that displays a string
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
