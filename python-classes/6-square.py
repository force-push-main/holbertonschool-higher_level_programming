#!/usr/bin/python3

"""this function declares a class for a square object"""


class Square:
    """this is a square object. It is empty"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(el, int) for el in value) or
                not all(el >= 0 for el in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            print('' * self.position[1])
            for i in range(self.size):
                print(' ' * self.position[0], end='')
                print('#' * self.size)
