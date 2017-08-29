#!/usr/bin/python3
class Rectangle:
    """ Sets width and height of Rectanle
    Attributes:
        number_of_instances (int): counter of instances
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Initilizes and calls respective setter method
        Args:
            width: int > 0
            height: int > 0
        """
        self.width, self.height = width, height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ width: has to be integer and greater than 0 """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height: has to be integer and greater than 0 """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns: area of Rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns: parimeter of Rectangle else 0 if height or width == 0 """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ String representation of Rectangle class.
        Returns: str rectangle in '#' form else empty string.
        """
        __string = ""

        if self.__width == 0 or self.__height == 0:
            return __string

        for h in range(self.__height):
            for w in range(self.__width):
                __string += '#'
            __string += '\n'
        return __string[:-1] #  avoid sending last newline character

    def __repr__(self):
        """ Returns: ClassName(arg1, arg2) """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Prints goodbye message """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
