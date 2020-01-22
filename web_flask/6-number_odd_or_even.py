#!/usr/bin/python3
""" Script that starts a flask app
"""
from flask import Flask, render_template
app = Flask('__name__', template_folder='templates')


@app.route('/', strict_slashes=False)
def Home():
    """ Function for / route
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def Hbnb():
    """ Function for /hbnb route
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def PrintText(text):
    return "C {}".format(text.replace('_', ' '))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def PrintText_2(text="is_cool"):
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def IsNumber(n):
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def Template_5(n):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def OddOrEven(n):
    if n % 2 == 0:
        string = "is even"
    else:
        string = "is odd"
    return render_template('6-number_odd_or_even.html', n=n, string=string)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
