#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import DateTime, String
from sqlalchemy.orm import declarative_base, mapped_column
import os

storage_type = os.environ.get('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if storage_type == 'db':
        id = mapped_column(String(60), primary_key=True, sort_order=-1)
        created_at = mapped_column(DateTime, default=datetime.utcnow,
                                   nullable=False, sort_order=-1)
        updated_at = mapped_column(DateTime, default=datetime.utcnow,
                                   nullable=False, sort_order=-1)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            """storage.new(self)"""
        else:
            # Will be formatted in iso format in to_dict()
            if 'updated_at' not in kwargs:
                self.created_at = datetime.now()
            if 'created_at' not in kwargs:
                self.updated_at = datetime.now()
            for key, value in kwargs.items():
                if key == 'updated_at':
                    setattr(
                               self, key,
                               datetime.strptime(
                                                    kwargs['updated_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f'
                                                )
                           )
                elif key == 'created_at':
                    setattr(
                               self,
                               key,
                               datetime.strptime(
                                                    kwargs['created_at'],
                                                    '%Y-%m-%dT%H:%M:%S.%f'
                                                )
                           )
                elif key != '__class__':
                    setattr(self, key, value)
                # also set an id
                self.id = str(uuid.uuid4())

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        # return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)
        my_dict = {}
        my_dict.update(self.to_dict())
        del my_dict['__class__']
        return '[{}] ({}) {}'.format(cls, self.id, my_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']
        return dictionary

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        storage.delete(self)
