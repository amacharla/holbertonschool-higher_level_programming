#!/usr/bin/python3
""" Module with method ``load_from_json_file`` """


def load_from_json_file(filename):
    """
    Deserializees json file -> object
    Returns: object
    """

    assert (type(filename) is str), "filename is not string"

    with open(filename, "r") as a_file:
        import json
        return json.load(a_file)
