#!/usr/bin/python3
# 2-matrix_divided.py

def div_el(el, div):
    if not isinstance(el, int) and not isinstance(el, float):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    else:
        return round(el / div, 2)

def matrix_divided(matrix, div):
    if not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in range(len(matrix) - 1):
        if len(matrix[i]) is not len(matrix[i + 1]):
            raise TypeError("Each row of the matrix must have the same size")
    new_matrix = [list(map(lambda el: div_el(el, div), row)) for row in matrix]
    return new_matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)