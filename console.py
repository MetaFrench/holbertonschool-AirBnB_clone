#!/usr/bin/python3
"""Module 8-rectangle
Creating class Rectangle that inherits from
BaseGeometry(8-base_geometry.py)
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Creates class Gemoetry"""

    def __init__(self, width, height):
        """Initializes Rectangle class"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""

        return self.__width * self.__height

    def __str__(self):
        """Returns a formatted string."""

        return str("[Rectangle] {}/{}".format(self.__width, self.__height))
