#!/usr/bin/python3
"""Starts a Flask web application, and defines routes.
"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
import os
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def display_states():
    """Displays all States"""
    states_dict = storage.all(State)
    sorted_dict = dict(sorted(states_dict.items(), key=lambda item:
                       item[1].name))
    return render_template('7-states_list.html', states=sorted_dict)


@app.route('/states/<id>', strict_slashes=False)
def cities_by_state(id):
    """Displays all states with their respective cities"""
    storage_type = os.getenv('HBNB_TYPE_STORAGE')
    my_state = None
    my_cities = None
    # Get all State objects
    states_dict = storage.all(State)  # a dictionary
    for state_object in states_dict.values():
        if state_object.id == id:
            state_cities = state_object.cities
            # sort cities
            sorted_cities = sorted(state_cities, key=lambda city: city.name)
            my_state = state_object
            my_cities = sorted_cities
            break
    return render_template('9-states.html', my_state=my_state,
                           my_cities=my_cities)


@app.teardown_appcontext
def remove_current_session(exception):
    """Removes current SQLAlchemy session"""
    if exception:
        print(f'An error occured: {exception}')
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
