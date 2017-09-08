#!/usr/bin/python3
""" Module with method ``write_file`` """


def write_file(filename="", text=""):
    """
    writes ``text`` to file ``filename``
    Returns: number of bytes written

    """

    assert (type(filename) is str), "Filename is not string"
    assert (type(text) is str), "Text is not string"

    with open(filename, "w", encoding='utf-8') as a_file:
        return a_file.write(text)
