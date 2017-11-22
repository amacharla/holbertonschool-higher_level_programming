#!/usr/bin/python3
"""
Technical Interview Prep:
Find a peak via divide and conqure
"""


def find_peak(list_of_integers):
    """ Wrapper function for reqursion
    Args:
        list_of_integers (list): list of unsorted integers
    Returns:
        int: local max
    """

    size = len(list_of_integers)

    if size == 0:  # list is empty
        return None
    if size == 1:  # only one number in list
        return list_of_integers[0]

    # recurse via divide and conqure helper function
    return divide_conquer(list_of_integers, 0, size - 1)
#                                              indexed


def divide_conquer(array, start, end):
    """ Recursion helper function
    Args:
        array (list): list of integers
        start (int): index of starting location
        end (int): index of ending location

    Returns:
        int: local max
        func: recursive call to function
    """

    mid = int((start + end) / 2)

    if start < mid < end:  # make sure more than 2 numbers

        if array[mid - 1] < array[mid] > array[mid + 1]:  # peak found
            return array[mid]

        if array[mid - 1] > array[mid]:  # left > pointer -> d&c left side
            return divide_conquer(array, start, mid)
        else:  # d&c right side
            return divide_conquer(array, mid, end)

    if array[start] > array[end]:  # only 2 number return the greater one
        return array[start]
    else:
        return array[end]
