#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        ''' size: Must be an int greater than 0 '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        ''' Return: current square area '''
        return self.__size ** 2
