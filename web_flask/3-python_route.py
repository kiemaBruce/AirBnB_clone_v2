#!/usr/bin/python3
"""Starts a Flask web application, and defines 3 routes.
"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root():
    """Defines what happens when the root directory is accesed.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Defines what happens when the /hbnb directory is accessed.
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_func(text):
    """Defines what happens when the /c/<text> directory is accessed.
    """
    # First replace all underscores with space
    my_str = text.replace('_', ' ')
    return f'C {my_str}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_func(text='is cool'):
    """Defines what happens when the /python/<text> directory is accesed.
    """
    my_str = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
