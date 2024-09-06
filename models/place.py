#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
import os
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

storage_type = os.environ.get('HBNB_TYPE_STORAGE')


if storage_type == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False),
                          mysql_charset='latin1'
                          )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    __table_args__ = {
            'mysql_charset': 'latin1'
    }

    if storage_type == 'db':
        user_id = Column(String(60), ForeignKey('users.id',
                         ondelete='CASCADE'), nullable=False)
        city_id = Column(String(60), ForeignKey('cities.id',
                         ondelete='CASCADE'), nullable=False)
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
        amenities = relationship("Amenity", secondary='place_amenity',
                                 viewonly=False,
                                 back_populates="place_amenities")
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """Returns list of Review instances with place_id equalts to the
            current Place.id"""
            my_reviews = []
            from models.places import Place
            from models import storage
            for key, value in storage.all(Review).items():
                if value.place_id == self.id:
                    my_reviews.append(value)
            return my_reviews

        @property
        def amenities(self):
            """Returns a list of Amenity instances based on the attribute
            amenity_ids that contains all Amenity.id linked to the place"""
            from models.amenity import Amenity
            from models import storage
            print(f'Name of storage class: {storage.__class__.__name__}')
            amenities_dict = storage.all(Amenity)
            amenity_instances = []
            for key, value in amenities_dict.items():
                if value.id in self.amenity_ids:
                    amenity_instances.append(value)
            return amenity_instances

        @amenities.setter
        def amenities(self, value):
            """Inserts Amenity.id into amenity_ids class attribute

            Arguments:
                value (Amenity): the Amenity object whose id is to be added to
                                 amenity_ids. If it is not an Amenity object
                                 then the function returns without doing
                                 anything.
            """
            from models.amenity import Amenity
            if (type(value) is Amenity):
                self.amenity_ids.append(value.id)
