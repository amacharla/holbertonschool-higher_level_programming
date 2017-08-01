#!/usr/bin/python3
for a in range(9):
    for b in range(9):
        if a != b:
            print("{:d}{:d}".format(a, b), end=", " if a != 8 and b != 9 else None)

