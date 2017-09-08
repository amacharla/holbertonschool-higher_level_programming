#!/usr/bin/python3
""" Module with method read_lines() """


def read_lines(filename="", nb_lines=0):
    """ Read required amout of lines from file """

    assert (type(filename) is str), "Filename is not string"

    with open(filename, "r", encoding='utf-8') as a_file:
        lines = [line for line in a_file]  # put all lines into list
        # handle negative line count
        nb_lines = len(lines) if nb_lines <= 0 else nb_lines
        print("".join(lines[:nb_lines]), end='')  # convert list to string and print
