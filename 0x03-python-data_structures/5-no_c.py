#!/usr/bin/python3
def no_c(my_string):
    for index, char in enumerate(my_string[:]):
        if char == 'c' or char == 'C':
            new_string = my_string[:index] + my_string[index + 1:]
    return (new_string)
