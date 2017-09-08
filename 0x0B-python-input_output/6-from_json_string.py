#!/usr/bin/python3
""" Module with method ``from_json_string`` """

def from_json_string(my_str):
    """
    Deserializing
    Returns: my_str -> object
    """

    assert (type(my_str) is str), "my_str is not string"
    import json
    return json.loads(my_str)
