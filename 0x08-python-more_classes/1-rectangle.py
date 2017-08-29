#!/usr/bin/python3
""" Module with Rectangle Class """

class Rectangle:
    """ Sets width and height of Rectanle """

    def __init__(self, width=0, height=0):
        """ Initilizes and calls respective setter method
        Args:
            width: int > 0
            height: int > 0
        """
        self.width, self.height = width, height

    @property
    def width(self):
        """ width: has to be integer and greater than 0 """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height: has to be integer and greater than 0 """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
