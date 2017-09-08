#!/usr/bin/python3
""" Module with method ``append_write`` """


def append_write(filename="", text=""):
    """
    appends ``text`` to file ``filename``
    Returns: number of bytes written

    """

    assert (type(filename) is str), "Filename is not string"
    assert (type(text) is str), "Text is not string"

    with open(filename, "a", encoding='utf-8') as a_file:
        return a_file.write(text)
