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

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.size):
                print('#' * self.size)

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
