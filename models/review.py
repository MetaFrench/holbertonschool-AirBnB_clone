#!/usr/bin/python3
"""has a class 'Review'"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class that defines a review"""

    place_id = ""
    user_id = ""
    text = ""
