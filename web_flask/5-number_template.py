#!/user/bin/python3
from flask import Flask, render_template

app = Flask('__name__', template_folder='templates')
@app.route('/', strict_slashes=False)
def Home():
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def Hbnb():
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

@app.route('/number_template/<int:n>')
def Template_5(n):
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
