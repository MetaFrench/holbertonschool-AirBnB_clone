#!/usr/bin/python3
"""module holds a class BaseModel"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """basemodel class for other classes"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'updated_at' or key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the self.updated at attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dict containing the instance attributes"""
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = type(self).__name__
        if type(my_dict['created_at']) is not str:
            my_dict['created_at'] = self.created_at.isoformat()
        if type(my_dict['updated_at']) is not str:
            my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
