#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        return [[num * num for num in row] for row in matrix]
    return
