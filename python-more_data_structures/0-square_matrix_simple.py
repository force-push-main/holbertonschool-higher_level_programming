#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared = matrix.copy()
    for i in range(len(squared)):
        for j in range(len(squared[i])):
            squared[i][j]**2
    return squared
