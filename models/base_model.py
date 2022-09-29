#!/usr/bin/python3
from uuid import uuid4
from datetime import datetime

class BaseModel:

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return f"[{type(self)}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()
