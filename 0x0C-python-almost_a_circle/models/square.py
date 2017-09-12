#!/usr/bin/python3
""" Module with Square class that inherates from Rectangle class """
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class inherated from Rectangle from Base """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initilize by sending args to Base cls & validating them """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Overrides default print behavior for Square class """
        #  format that get value by calling self
        return "[Square] ({0.id}) {0.x}/{0.y} - {0.width}".format(self)

    @property
    def size(self):
        """ Size setter and getter returns width """
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates attributes in class Rectangle """
        if len(args):  # if args is passed
            SaqAttr = iter(['size', 'x', 'y'])  # iter for next()
            for idx, arg in enumerate(args):
                if idx == 0:  # handles id
                    Base().__init__(arg)  # calls Bases Intit
                    continue
                try:  # argument validation
                    # calls respective setter method
                    setattr(self, next(SaqAttr), arg)
                except Exception as error:  # setter error msg
                    print(error)
        else:  # if kwargs is passed
            for key, value in kwargs.items():
                if key == id:  # handles id
                    Base().__init__(key)  # calls Bases intit
                    continue
                if hasattr(self, key):  # key validation
                    try:  # argument validation
                        # calls respective setter method
                        setattr(self, key, value)
                    except Exception as error:  # setter error msg
                        print(error)
                else:  # if key doesnt exist dont create attribute
                    continue

    def to_dictionary(self):
        """ Returns: dict of instances attributes """
        SaqAttr = ['id', 'size', 'x', 'y']  # get following attr
        newdict = {attr: getattr(self, attr) for attr in SaqAttr}
        return newdict
