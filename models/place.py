#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship


association_table = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id')),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'))
                          )


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
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
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

    @property
    def amenities(self):
        """Returns a list of Amenity instances based on the attribute
        amenity_ids that contains all Amenity.id linked to the place"""
        from models.amenity import Amenity
        from models.__init__ import storage
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
                         amenity_ids. If it is not an Amenity object then the
                         function returns without doing nothing.
        """
        from models.amenity import Amenity
        if (type(value) is Amenity):
            self.amenity_ids.append(value.id)
