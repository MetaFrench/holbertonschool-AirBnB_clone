#!/usr/bin/python3
"""module holds a class BaseModel"""
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """basemodel class for other classes"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the self.updated at attribute"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dict containing the instance attributes"""
        self.__dict__['__class__'] = type(self).__name__
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        return self.__dict__
