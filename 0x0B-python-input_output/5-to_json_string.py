#!/usr/bin/python3
""" Module with method ``to_json_string`` """

def to_json_string(my_obj):
    """
    Serializing
    Returns: JSON format <- ``my_obj``
    """

    import json
    return json.dumps(my_obj)
