#!/usr/bin/python3
"""
Module Contains: function inherits_from()
"""


def inherits_from(obj, a_class):
    """
    function determins if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class but not base class itself

    Returns: True if the object is exactly as subclass otherwise False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
