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
        """ Returns: list of dicts -> json str """

        l_d = list_dictionaries
        if type(l_d) is not list or len(l_d[0]) == 0 or l_d is None:
            return "[]"
        import json
        return json.dumps(l_d)

    @staticmethod
    def from_json_string(json_string):
        """ Returns: list <- json str """

        if len(json_string) == 0 or type(json_string) is not str:
            return []
        import json
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save instances attributes as dict -> json str -> json file """

        if list_objs is not None:
            clsAttr = ['id', 'width', 'height', 'size', 'x', 'y']  # get attr
            # get attr and convert them to dict and place them in list
            cls_list = [{attr: getattr(inst, attr) for attr in clsAttr
                        if hasattr(inst, attr)} for inst in list_objs]
        else:
            cls_list = [{}]  # writing to file an empty list

        with open("{}.json".format(cls.__name__), "w") as json_file:
            import json  # convert list of dict to json str and write to file
            json_file.write(cls.to_json_string(cls_list))
