#!/usr/bin/python3
""" Module with ``Base`` Class """


class Base():
    """ Base Class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initilizing Instance Counter """

        if id is None:  # increment instance and assign if id not passed
            type(self).__nb_objects += 1
            type(self).id = type(self).__nb_objects
        else:  # if id is passed then assign it to id
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns: json str of dict """

        l_d = list_dictionaries
        if type(l_d) is not list or len(l_d[0]) == 0 or l_d is None:
            return "[]"
        import json
        return json.dumps(l_d)
