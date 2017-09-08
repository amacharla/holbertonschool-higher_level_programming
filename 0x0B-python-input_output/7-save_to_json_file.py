#!/usr/bin/python3
""" Module with method ``from_json_string`` """

def save_to_json_file(my_obj, filename):
    """ Serializes object -> json file """

    assert (type(filename) is str), "Filename is not string"

    with open(filename, "w") as a_file:
        import json
        json.dump(my_obj, a_file)
