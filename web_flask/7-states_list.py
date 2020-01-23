#!/usr/bin/python3
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def CloseSession(self):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def StateList():
    objs = storage.all('State')
    return render_template('7-states_list.html', objs=objs)

if __name__ == '__main__':
    app.run()
