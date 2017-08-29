#!/usr/bin/python3
""" Method with LockedClass """

class LockedClass():
    """ Locked Class can only have attribute called `firs_name` """

    __slots__ = ['first_name']
