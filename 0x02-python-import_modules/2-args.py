#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len = len(argv) - 1
    print("{:d} argument{}".format(len, "." if len <= 1 else "s:"))
    for index, value in enumerate(argv[1:], 1):
        print("{:d}:".format(index), value)
