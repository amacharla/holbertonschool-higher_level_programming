#!/usr/bin/python3
"""
Module Contains: function is_kind_of_class()
"""


def is_kind_of_class(obj, a_class):
    """
    function that determins if `obj` is instance of `a_class`

    Returns: True if the object is exactly an instance of the specified class
    otherwise False
    """
    return isinstance(obj, a_class)
