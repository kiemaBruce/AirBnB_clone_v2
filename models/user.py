#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'
    if storage_type == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False, server_default="NULL")
        last_name = Column(String(128), nullable=False, server_default="NULL")
        places = relationship("Place", back_populates="user",
                              cascade="all, delete")
        reviews = relationship("Review", back_populates="user",
                               cascade="all, delete")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
