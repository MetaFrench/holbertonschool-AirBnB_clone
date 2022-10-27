#!/usr/bin/python3
"""engine for running sqlalchemy"""
import os
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session, scoped_session
from models.base_model import Base
from models.state import State
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker


class DBStorage():
    """dbstorage engine class"""

    __engine = None
    __session = None
    
    def __init__(self):
        user = os.getenv("HBNB_MYSQL_USER")
        password = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, password, host, database),
                                      pool_pre_ping=True)
        if os.getenv("HBNB_ENV") == 'test':
            Base.metadata.dropall(self.__engine)

    def all(self, cls=None):
        """lists all objects of class, or objects of all classes
        if none specified"""
        classes = {'User': User, 'State': State, 'City': City,
               'Amenity': Amenity, 'Place': Place, 'Review': Review}
        dict_all = {}
        if cls is None:
            for classname in classes.values():
                result = self.__session.query(classname).all()
                for obj in result:
                    dict_all[f'{type(obj).__name__}.{obj.id}'] = obj
        else:
            result = self.__session.query(classes[cls]).all()
            for obj in result:
                dict_all[f'{type(obj).__name__}.{obj.id}'] = obj
        return dict_all

    def new(self, obj):
        """adds object to session"""
        self.__session.add(obj)

    def save(self):
        """commits the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object from session"""
        if obj is not None:
            self.__session.delete()

    def reload(self):
        """create all tables in database, creates a session"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        self.__session = scoped_session(session_factory)
