#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints "my name first_name last_name"

    Arguments:
        first_name: string
        last_name: string or empty

    Raises:
        TypeError: both arguments are not string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctet.testmod()
