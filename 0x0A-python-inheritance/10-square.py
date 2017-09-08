#!/usr/bin/python3
"""
Module Contains:
    Base: BaseGeometry
    Inhertance: Rectangle()
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class that inherits from BaseGeometry """

    def __init__(self, size):
        """ initilizes size """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)
