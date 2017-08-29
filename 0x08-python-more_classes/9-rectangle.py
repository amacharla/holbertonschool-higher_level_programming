#!/usr/bin/python3
class Rectangle:
    """ Sets width and height of Rectangle
    Attributes:
        number_of_instances (int): counter of instances
        print_symbol (str): modify symbol to print Rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ Initilizes and calls respective setter method
        Args:
            width: int > 0
            height: int > 0
        Updates Instance counter
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
        Returns: str rectangle in @print_symbol form else empty string.
        """
        __string = ""

        if self.__width == 0 or self.__height == 0:
            return __string

        for h in range(self.__height):
            for w in range(self.__width):
                __string += str(self.print_symbol)
            __string += '\n'
        return __string[:-1]  # avoid sending last newline character

    def __repr__(self):
        """ Returns: ClassName(arg1, arg2) """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Prints goodbye message
        Decrement Instance counter """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Returns bigger rectangle based of area
        Args:
            rect_1: type Rectangle
            rect_2: type Rectangle
        Raises:
            TypeError: if rect_1 or rect_2 is not an instance of Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """ Returns: new Rectangle instance with equal width and height """
        return cls(size, size)
