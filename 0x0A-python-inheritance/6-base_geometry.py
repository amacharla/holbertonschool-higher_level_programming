#!/usr/bin/python3
"""
Module Contains:
    Base: BaseGeometry
"""


class BaseGeometry():
    """ Base Class with `area` method """

    def area(self):
        """ Raises: Exception when `area` is called """
        raise Exception("area() is not implemented")
