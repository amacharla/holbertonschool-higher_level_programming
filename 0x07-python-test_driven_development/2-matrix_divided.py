#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides every element in matrix by div varable

    Arguments:
        matrix: a list of lists of equal size made up of numbers
        div: a non zero number

    Returns: New matrix with computed result

    Raises:
        TypeError: if matrix element is not number
            or matrix is not list of lists
            or list len is not equal
        ZeroDivisionError: if div is 0
    """

    if type(div) is not int and type(dive) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    matrixchk = type(matrix) is list
    if matrixchk:
        listlen = len(matrix[0])
        lenchk = all(list(map(lambda lists: len(lists) == listlen, matrix)))
        listchk = all(list(map(lambda lists: type(lists) is list, matrix)))
        intchk = all(type(element) is int or type(element) is float
                     for listss in matrix for element in listss)

    if not all((listchk, intchk, matrixchk)):
        raise TypeError('matrix must be a matrix (list of lists) of\
            integers/floats')
    if lenchk is False:
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = []
    for lists in matrix:
        new_matrix.append(list(map(lambda num: float(format((num / div),
                                                            ".02f")), lists)))
    return new_matrix
