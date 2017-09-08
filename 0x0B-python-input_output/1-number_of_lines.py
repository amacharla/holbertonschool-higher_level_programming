#!/usr/bin/python3
""" Module contains method ``number_of_lines`` """


def number_of_lines(filename=""):
    """ Returns: line count of file """

    assert (type(filename) is str), "Filename passed is not string"

    with open(filename, "r", encoding='utf-8') as a_file:
        return sum(1 for line in a_file)  # sum(+1 for each line)
