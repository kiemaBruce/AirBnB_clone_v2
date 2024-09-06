#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import String
from sqlalchemy.orm import relationship, mapped_column


storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    __table_args__ = {
        'mysql_charset': 'latin1'
    }
    if storage_type == 'db':
        """
        cities = relationship("City", back_populates="state",
                                cascade="all, delete")
        """
        name = mapped_column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """Returns the list of city instances with state_id equal to
            current State.id, that is, a list of City objects from
            storage linked to the current State"""
            my_cities = []
            from models.city import City
            from models import storage
            for key, value in storage.all(City).items():
                if value.state_id == self.id:
                    my_cities.append(value)
            return my_cities
