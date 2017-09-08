#!/usr/bin/python3
"""
Module Contains:
    Class: MyList()
        Funciton: print_sorted
"""


class MyList(list):
    """ A class that that inherits from `list` """

    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        """ printed sorted list """
        print(sorted(self))
