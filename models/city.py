#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    __table_args__ = {
            'mysql_charset': 'latin1'
    }

    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60),
                          ForeignKey('states.id', ondelete='CASCADE'),
                          nullable=False)
        places = relationship("Place", back_populates="cities",
                              cascade="all, delete")
        # state = relationship('State', back_populates='cities')
    else:
        state_id = ""
        name = ""
