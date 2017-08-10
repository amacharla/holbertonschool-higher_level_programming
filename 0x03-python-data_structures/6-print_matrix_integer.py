#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            if row != []:
                for i, num in enumerate(row, 1):
                    ending = ' ' if i != len(row) else '\n'
                    print("{:d}".format(num), end=ending)
            else:
                print()
