#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        num = [num for row in matrix for num in row]
        for i in range(len(num)):
            if i % 3 == 0:
                [print(num[set], end=" ") for set in range(i)]
