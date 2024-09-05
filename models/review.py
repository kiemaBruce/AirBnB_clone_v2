#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = "reviews"
    __table_args__ = {
            'mysql_charset': 'latin1'
    }
    if storage_type == 'db':
        text = Column(String(1024), nullable=False)
        place_id = Column(String(60), ForeignKey("places.id",
                          ondelete='CASCADE'), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id",
                         ondelete='CASCADE'),
                         nullable=False)
        user = relationship("User", back_populates="reviews")
    else:
        place_id = ""
        user_id = ""
        text = ""
