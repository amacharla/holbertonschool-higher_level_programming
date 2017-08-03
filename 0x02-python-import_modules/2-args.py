#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len = len(argv) - 1
    if len == 0:
        end = "."
    elif len == 1:
        end = ":"
    else:
        end = "s:"
    print("{:d} argument{}".format(len, end))
    for index, value in enumerate(argv[1:], 1):
        print("{:d}:".format(index), value)
