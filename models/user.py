#!/usr/bin/python3
"""Has a class 'User'"""
from models.base_model import BaseModel


class User(BaseModel):
    """CLass that defines a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
