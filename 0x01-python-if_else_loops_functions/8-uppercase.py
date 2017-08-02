#!/usr/bin/python3
def uppercase(str):
    for i in str[:]:
        char = ord(i)
        if char >= 97 and char <= 122:
            print("{:s}".format(chr(char - 32)), end="")
        else:
            print(i, end="")
    print()
