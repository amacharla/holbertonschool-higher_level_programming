#!/usr/bin/python3
""" Module with Student class """


class Student():
    """ to_json method """

    def __init__(self, first_name, last_name, age):
        """ initilizes Student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Returns attributes of this class """
        if attrs is None:  #if no attrs specified
            return self.__dict__.copy()
        return {key: value for key, value in self.__dict__.items() if key in attrs}
