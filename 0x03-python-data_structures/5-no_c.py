#!/usr/bin/python3
def no_c(my_string):
    new_list = []
    for char in my_string:
        if char not in "cC":  # checks if char is c or C
            new_list.append(char)  # stores char in list
# turn list into mutable type by getting rid of ", " makes it not a list
    return ("".join(new_list))
