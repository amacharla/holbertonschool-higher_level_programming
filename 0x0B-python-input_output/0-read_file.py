#!/usr/bin/python3
""" Module with method read_file """


def read_file(filename=""):
    """ Opens and Reads and Prints contents of file """

    assert (type(filename) is str), "Filename passed is not string"

    with open(filename, encoding='utf-8') as a_file:
        print(a_file.read())
