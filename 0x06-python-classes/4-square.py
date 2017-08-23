#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """
        Calls size.setter func
        Args:
            size: must be int and greater than 0
        """
        self.size = size

    def area(self):
        """ Returns: current square area """
        return self.__size ** 2

    @property
    def size(self):
        """ Getter method
        Returns: size """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Args:
                value: must be int and greater than 0
        Raises:
            TypeError: if size is not int
            ValueError: size is less than 0
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
