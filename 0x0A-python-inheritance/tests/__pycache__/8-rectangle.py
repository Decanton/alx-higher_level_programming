#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """this class represents a base geometry"""

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """a class that defines rectangle"""
    def __init__(self, width, height):

        self.__width = width
        self.__height = height
        self.__width = 0
        self.__height = 0

        self.integer_validator("width", width)
        self.integer_validator("height", height)
