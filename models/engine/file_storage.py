#!/usr/bin/python3
"""has a class FileStorage that sFileStorage"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """FileStorage"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """returns __objects dict"""
        return FileStorage.__objects

    def new(self, obj):
        """adds obj to __objects dict"""
        FileStorage.__objects[f'{type(obj).__name__}.{obj.id}'] = obj

    def save(self):
        """serializes __objects dict to json file"""
        my_dict = {}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            for key, value in FileStorage.__objects.items():
                my_dict[key] = value.to_dict()
            f.write(json.dumps(my_dict))

    def reload(self):
        """deserializes the json file into __objects dict"""
        try:
            with open(FileStorage.__file_path, encoding='utf-8') as f:
                all_objs = json.loads(f.read())
                for key, value in all_objs.items():
                    FileStorage.__objects[key] = \
                        eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
        except json.decoder.JSONDecodeError:
            pass
