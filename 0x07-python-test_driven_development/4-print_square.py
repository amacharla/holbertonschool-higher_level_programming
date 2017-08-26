#!/usr/bin/python3
def print_square(size):
    """ Print a square with the character #
    Arguments:
        Size: is the length of the square, must be int
    Raises:
        TypeError: if size is not Integer,Float and less than zero
        ValueError: size is less than 0
    """
    if type(size) != int and type(size) != float:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    [print('#' * size) for i in range(size)]
