#!/usr/bin/python3
"""
Module Contains:
    Base: BaseGeometry
    Inhertance: Rectangle()
"""


class BaseGeometry():
    """ Base Class with `area` and integer_validator methods """

    def area(self):
        """ Raises: Exception when `area` is called """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Raises:
            TypeError: value is not int
            ValueError: value less or = 0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Class that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ initilizes width and height """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
