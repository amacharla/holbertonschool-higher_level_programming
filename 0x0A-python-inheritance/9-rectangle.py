#!/usr/bin/python3
"""
Module Contains:
    Base: BaseGeometry
    Inhertance: Rectangle() and Square()
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Class that inherits from BaseGeometry """

    def __init__(self, width, height):
        """ initilizes width and height """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns: area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ prints [Rectange] width/height """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
