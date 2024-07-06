#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id', ondelete='CASCADE'),
                     nullable=False)
    user_id = Column(String(60), ForeignKey('users.id', ondelete='CASCADE'),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True, server_default=None)
    number_rooms = Column(Integer, nullable=False, server_default="0")
    number_bathrooms = Column(Integer, nullable=False, server_default="0")
    max_guest = Column(Integer, nullable=False, server_default="0")
    price_by_night = Column(Integer, nullable=False, server_default="0")
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    user = relationship("User", back_populates="places")
    cities = relationship("City", back_populates="places")
    reviews = relationship("Review", back_populates="place",
                           cascade="all, delete-orphan")
    amenity_ids = []

    @property
    def reviews(self):
        """Returns list of Review instances with place_id equalts to the
        current Place.id"""
        my_reviews = []
        from models.places import Place
        from models.__init__ import storage
        for key, value in storage.all(Review).items():
            if value.place_id == self.id:
                my_reviews.append(value)
        return my_reviews
