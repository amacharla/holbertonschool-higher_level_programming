#!/usr/bin/python3

"""
Module Contains:
    Funciton: lookup
"""


def lookup(obj):
    """ Returns: all attributes of `obj` """

    return list(obj.__dict__)
