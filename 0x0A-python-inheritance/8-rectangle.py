#!/usr/bin/python3
"""
Module Contains:
    Base: BaseGeometry
    Inhertance: Rectangle()
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
