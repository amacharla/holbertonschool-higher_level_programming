#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        Args:
            size: must be int and greater than 0
        Raises:
            TypeError: if size is not int
            ValueError: size is less than 0
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position[0]) != int and type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
# SIZE------------------------------------------------------------------------

    @property
    def size(self):
        """
        Getter method
        Returns: size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter method
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
# Position--------------------------------------------------------------------

    @property
    def position(self):
        """ Getter method
        Returns: position """
        return self.__position

    @position.setter
    def position(self, position):
        """ setter method
        Args:
                position: tuple must be 2 positive int
        Raises:
            TypeError: position must be a tuple of 2 positive integers
        """
        if type(position.args) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
# Special--------------------------------------------------------------------

    def area(self):
        """ Returns: current square area """
        return self.__size ** 2

    def my_print(self):
        """ prints square visually with # at position(x, y) """
        if self.__size == 0:
            print()
        else:
            x, y = self.__position[0], self.__position[1]
            [print() for i in range(y)]  # goes down
            for j in range(self.__size):
                print(" " * x, end='')  # goes right set position
                print("#" * self.__size)  # prints square horozantally then \n
