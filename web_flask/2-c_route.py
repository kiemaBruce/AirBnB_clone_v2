#!/usr/bin/python3
"""Starts a Flask web application, and defines  routes.
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
    my_str = text[:]
    for index, char in enumerate(my_str):
        if char == '_':
            my_str = my_str[:index] + ' ' + text[index + 1:]
    return f'C {my_str}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
