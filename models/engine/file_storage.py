#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            filtered_dict = {}
            for key, value in FileStorage.__objects.items():
                cls_name = cls.__name__
                if cls_name in key:
                    filtered_dict.update({key: value})
        """return FileStorage.__objects"""
        if cls:
            return filtered_dict
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review, 'Place': Place
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Deletes an instance if it is inside __objects"""
        if obj is None:
            return
        del_key = None
        for key, value in self.all().items():
            if obj == value:
                del_key = key
                """del self.all()[key]"""
                break
        del self.all()[key]

    def close(self):
        """Reloads the app state"""
        self.reload()
