#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__, self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        self.__dict__['class'] = self.__class__
        self.created_at.isoformat()
        self.updated_at.isoformat()
        return self.__dict__

