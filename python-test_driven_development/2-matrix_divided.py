#!/usr/bin/python3
# 2-matrix_divided.py
"""divides matrix"""


def div_el(el, div):
    """helper function to divide els in array"""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(el, int) and not isinstance(el, float):
        raise TypeError(msg)
    else:
        return round(el / div, 2)


def matrix_divided(matrix, div):
    """divides all elements in matrix by div and returns new matrix"""
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix) - 1):
        if len(matrix[i]) is not len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    new_matrix = [list(map(lambda el: div_el(el, div), row)) for row in matrix]
    return new_matrix
