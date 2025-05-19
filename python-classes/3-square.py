#!/usr/bin/python3

"""this function declares a class for a square object"""


class Square:
    """this is a square object. It is empty"""
    def __init__(self, size=0):
        self.__size = None
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size ** 2
