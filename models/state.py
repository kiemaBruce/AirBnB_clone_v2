#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    storage_type = os.environ.get('HBNB_TYPE_STORAGE')

    if storage_type != 'db':
        @property
        def cities(self):
            """Returns the list of city instances with state_id equal to
            current State.id, that is, a list of City objects from
            storage linked to the current State"""
            my_cities = []
            from models.city import City
            from models.__init__ import storage
            for key, value in storage.all(City).items():
                if value.state_id == self.id:
                    my_cities.append(value)
            return my_cities
