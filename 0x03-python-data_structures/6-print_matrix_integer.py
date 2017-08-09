#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for row in matrix:
            for i, num in enumerate(row, 1):
                print("{:d}".format(num), end=" " if i != len(row) else '\n')
