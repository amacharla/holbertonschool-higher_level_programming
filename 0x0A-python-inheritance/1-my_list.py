#!/usr/bin/python3
"""
Module Contains:
    Class: MyList()
        Funciton: print_sorted
"""


class MyList(list):
    """ A class that that inherits from `list` """

    def print_sorted(self):
        """ printed sorted list """
        print(sorted(self))
