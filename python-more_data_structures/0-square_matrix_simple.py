#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared = matrix.copy()
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = matrix[i][j]**2
    return squared
