#!/usr/bin/python3
"""
Module Contains:
    Base: BaseGeometry
    Inhertance: Rectangle() and Square()
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

    def area(self):
        """ Returns: area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ prints [Rectange] width/height """
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(BaseGeometry):
    """ Class that inherits from BaseGeometry """

    def __init__(self, size):
        """ initilizes size """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ Returns: area of Square """
        return self.__size ** 2

    def __str__(self):
        """ string rep: [Square] size/size """
        return "[Square] {0:d}/{0:d}".format(self.__size)
