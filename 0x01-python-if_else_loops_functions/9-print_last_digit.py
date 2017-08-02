#!/usr/bin/python3
def print_last_digit(number):
    num = str(number)
    lastdigit = int(num[-1])
    print(lastdigit, end="")
    return lastdigit
