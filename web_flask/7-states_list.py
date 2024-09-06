#!/usr/bin/python3
"""Starts a Flask web application, and defines routes.
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def display_states():
    """Displays all States"""
    states_dict = storage.all(State)
    sorted_dict = dict(sorted(states_dict.items(), key=lambda item:
                       item[1].name))
    return render_template('7-states_list.html', states=sorted_dict)


@app.teardown_appcontext
def remove_current_session(exception):
    """Removes current SQLAlchemy session"""
    if exception:
        print(f'An error occured: {exception}')
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
