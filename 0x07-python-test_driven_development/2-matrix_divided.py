#!/usr/bin/python3
"""Write a function that divide all elements of a matrix"""


def matrix_divided(matrix, div):
    if type(matrix) is not list:
        raise TypeError("matrix must be an matrix (list of+                lists) of integers/floats")
    size = None
    for i in matrix:
        if type(i) is not list:
            raise TypeError("matrix must be an matrix (list of lists) of integers/floats")
        if size is None:
            size = len(i)
        elif size != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for x in i:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be an matrix (list of lists) of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a member")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in x] for x in matrix]
