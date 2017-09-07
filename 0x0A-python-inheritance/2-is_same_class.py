#!/usr/bin/python3
"""
Module Contains: function is_same_class()
"""


def is_same_class(obj, a_class):
    """
    Function that determins if `obj` is of type `a_class`

    Returns: True if the object is same type as specified class
    otherwise False
    """
    return type(obj) == a_class
