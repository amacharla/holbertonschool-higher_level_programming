#!/usr/bin/python3
""" Module with ``Base`` Class """
import json


class Base():
    """ Base Class """

    __nb_objects = 0

    def __init__(self, id=None):
        """ Initilizing Instance Counter """

        if id is None:  # increment instance and assign if id not passed
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:  # if id is passed then assign it to id
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns: list of dicts -> json str """

        l_d = list_dictionaries
        if l_d is None:
            return "[]"
        return json.dumps(l_d)

    @staticmethod
    def from_json_string(json_string):
        """ Returns: list <- json str """

        if len(json_string) == 0 or json_string is None:
            return []  # if json_string is empty
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save instances attributes as dict -> json str -> json file """

        cls_list = []

        if list_objs is not None:
            # get attr and convert them to dict and place them in list
                [cls_list.append(obj.to_dictionary()) for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w") as json_file:
            # convert list of dict to json str and write to file
            json_file.write(cls.to_json_string(cls_list))

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance of class with given arguments
        Uses update() instead of because if class doesnt contain required
        arguments it wont spit out an error and return a proper object

        Returns: instance of class with `dictionary` attributes
        """
        dummy = cls(5, 5) if cls.__name__ is "Rectangle" else cls(5)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns: list of instances """

        try:  # if opening file fails or json str is empty and fails
            with open("{}.json".format(cls.__name__), "r") as json_file:
                # read file and convert json string -> list of dict
                clsdict = cls.from_json_string(json_file.read())
        except:  # if no file exist or json file is empty return empty list
            return []
        else:  # send cls.dict from list of dict and create instance
            return [cls.create(**attr) for attr in clsdict]
