#!/usr/bin/python3
""" Technical Interview Prep: Find a peak """


def find_peak(list_of_integers):
    """ Wrapper function for reqursion """

    size = len(list_of_integers)

    if size == 0: return None
    if size == 1: return list_of_integers[0]

    return divide_conquer(list_of_integers, 0, size - 1)


def divide_conquer(array, start, end):
    """recursion function"""

    mid = (start + end) / 2



