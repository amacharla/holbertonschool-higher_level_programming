#!/usr/bin/python3
""" Module contains method ``number_of_lines`` """


def number_of_lines(filename=""):
    """ Returns: line count of file """

    assert (type(filename) is str), "Filename passed is not string"

    with open(filename, "r", encoding='utf-8') as a_file:
        for lineNum, line in enumerate(a_file):
            pass
    return lineNum + 1  # accounts for index
