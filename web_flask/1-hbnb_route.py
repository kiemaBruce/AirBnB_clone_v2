#!/usr/bin/python3
"""Starts a Flask web application, and defines 2 routes.
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
