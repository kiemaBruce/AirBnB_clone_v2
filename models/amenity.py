#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import String
from sqlalchemy.orm import relationship, mapped_column


storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    __tablename__ = "amenities"
    __table_args__ = {
            'mysql_charset': 'latin1'
    }

    if storage_type == 'db':
        name = mapped_column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary='place_amenity',
                                       back_populates="amenities")
    else:
        name = ""
