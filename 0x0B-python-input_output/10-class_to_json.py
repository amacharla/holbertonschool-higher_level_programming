#!/usr/bin/python3
""" Module with class_to_json method """


def class_to_json(obj):
    """ Returns: all objects attributes """
    return obj.__dict__.copy()
