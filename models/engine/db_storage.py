#!/usr/bin/python3
""" New Engine DBStorage """

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """Definition of DBStorage attributes and methods

    Attributes:
        __engine: the connection engine.
        __session: the current session.
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initiates instance attributes"""
        user = os.environ.get('HBNB_MYSQL_USER')
        pwd = os.environ.get('HBNB_MYSQL_PWD')
        host = os.environ.get('HBNB_MYSQL_HOST')
        database = os.environ.get('HBNB_MYSQL_DB')
        my_env = os.environ.get('HBNB_ENV')
        engine_url = f'mysql+mysqldb://{user}:{pwd}@{host}:3306/{database}'
        self.__engine = create_engine(engine_url, pool_pre_ping=True)
        """Drop all tables if env is equal to test"""
        if my_env == "test":
            metadata = MetaData()
            # Reflect existing db structure
            metadata.reflect(bind=self.__engine)
            # Drop all tables
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Queries on the current database session all objects depending on the
        class name cls

        Arguments:
            cls (object): The class whose instances are to be returned.

        Returns:
            dict: a dictionary containing the <class-name>.<object-id> as the
                  key, and the object as the value.
        """
        results_list = []
        if cls is not None:
            # Dictionary containing results
            results_list.extend(self.__session.query(cls).all())
        else:
            from models.amenity import Amenity
            from models.user import User
            from models.state import State
            from models.city import City
            from models.place import Place
            from models.review import Review
            """
            classes = {"Amenity": Amenity, "User": User, "State": State,
                       "City": City, "Place": Place, "Review": Review}
            """
            classes = [Amenity, User, State, City, Place, Review]
            for item in classes:
                results_list.extend(self.__session.query(item).all())
        results_dict = {}
        for obj in results_list:
            key = f"{obj.__class__.__name__}.{obj.id}"
            results_dict.update({key: obj})
        return results_dict

    def new(self, obj):
        """Adds the object to the current database session

        Arguments:
            obj (object): the object to be added to the current database
                          session.
        """
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Deletes obj from the current database session if obj is not None

        Arguments:
            obj (object): the object to be deleted.
        """
        from models.amenity import Amenity
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review
        classes = {"Amenity": Amenity, "User": User, "State": State,
                   "City": City, "Place": Place, "Review": Review}
        if obj is not None:
            obj_cls = None
            for key, value in classes.items():
                if key == obj.__class__.__name__:
                    obj_cls = classes[key]
            # query to get the object to be deleted
            query = self.__session.query(obj_cls).filter(obj_cls.id == obj.id)
            # delete
            query.delete()
            # commit
            self.save()

    def reload(self):
        """Creates all tables in the database. Also creates the current
        database session self.__session"""
        from models.base_model import BaseModel
        from models.base_model import Base
        from models.amenity import Amenity
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.review import Review
        from models.place import association_table

        """ Logging
        import logging
        logging.basicConfig()
        logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
        """

        Base.metadata.create_all(self.__engine)  # create all tables
        session_factory = sessionmaker(
                                       bind=self.__engine,
                                       expire_on_commit=False
                                      )
        Session = scoped_session(session_factory)
        self.__session = Session()
