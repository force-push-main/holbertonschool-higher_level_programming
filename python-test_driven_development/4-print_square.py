#!/usr/bin/python3
"""function prints square"""


def print_square(size):
    """function that prints square of size*size"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print(f'#' * size)
