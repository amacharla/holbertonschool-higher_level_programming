#!/usr/bin/python3
""" Module with method read_lines() """


def read_lines(filename="", nb_lines=0):
    """ Read required amout of lines from file """

    assert (type(filename) is str), "Filename is not string"

    with open(filename, "r", encoding='utf-8') as a_file:
        if nb_lines <= 0:  # read enitre file
            print(a_file.read(), end='')
        else:  # read individual lines
            [print(a_file.readline(), end='') for line_num in range(nb_lines)
                if line_num != nb_lines]
