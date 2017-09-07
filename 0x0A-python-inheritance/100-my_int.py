#!/usr/bin/python3
""" Module with class MyInt() """


class MyInt(int):
    """ Class is an instance of int and overides comparision behavior """

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the default Not Equals behavior"""
        return super().__eq__(other)
