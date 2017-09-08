#!/usr/bin/python3

def read_lines(filename="", nb_lines=0):

    assert (type(filename) is str), "Filename is not string"

    with open(filename, encoding='utf-8') as a_file:
        for line in range(nb_lines):
            print
