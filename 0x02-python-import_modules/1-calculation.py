#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a, b = 10, 5
    print("{0:d} {1:s} {2:d} = {3:d}".format(a, "+", b, add(a, b)))
    print("{0:d} {1:s} {2:d} = {3:d}".format(a, "-", b, sub(a, b)))
    print("{0:d} {1:s} {2:d} = {3:d}".format(a, "*", b, mul(a, b)))
    print("{0:d} {1:s} {2:d} = {3:d}".format(a, "/", b, div(a, b)))
