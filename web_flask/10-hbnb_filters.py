#!/usr/bin/python3
"""Starts a Flask web application, and defines routes.
"""

from flask import Flask
from flask import render_template
from models import storage
from models.amenity import Amenity
from models.state import State
from models.city import City
import os
from sqlalchemy.exc import SQLAlchemyError

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displays all cities of a state"""
    storage_type = os.getenv('HBNB_TYPE_STORAGE')
    # a dict where the key is the state_name.id, and the
    # value is a list of cities in that state
    cities_dict = {}
    # Get all State objects
    states_dict = storage.all(State)  # a dictionary
    states_sorted = dict(sorted(states_dict.items(), key=lambda item:
                         item[1].name))
    for state_object in states_sorted.values():
        # A list of city objects for the current State
        my_cities = state_object.cities
        # sort cities
        sorted_cities = sorted(my_cities, key=lambda city: city.name)
        # store state and its cities in a dict
        cities_dict[state_object] = sorted_cities
    # Get all amenities
    amenities_dict = storage.all(Amenity)
    # Store amenity names in list, because that's all we need
    amenitiy_names = []
    for amenity_obj in amenities_dict.values():
        amenity_names.append(amenity_obj.name)
    return render_template('8-cities_by_states.html',
                           states_n_cities=cities_dict,
                           amenity_names=amenity_names)


@app.teardown_appcontext
def remove_current_session(exception):
    """Removes current SQLAlchemy session"""
    if exception:
        print(f'An error occured: {exception}')
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
