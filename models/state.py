#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    name = ""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Returns the list of city instances with state_id equal to current
        State.id"""
        my_cities = []
        from models.city import City
        from models.__init__ import storage
        for key, value in storage.all(City).items():
            if value.state_id == State.id:
                my_cities.append(value)
        return my_cities
