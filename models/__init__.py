"""initializes models module"""
from models.engine.file_storage import FileStorage
from models import base_model
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()
