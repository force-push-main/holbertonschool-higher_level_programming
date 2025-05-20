#!/usr/bin/python3

"""a function that creates a class called rectangle"""


class Rectangle:
    """an class for a rectangle object"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if (self.__height != 0 and
                self.__width != 0):
            return self.__height * 2 + self.__width * 2
        else:
            return 0

    def __str__(self):
        if (self.__height == 0 or
                self.__width == 0):
            return ""
        str = ""
        for _ in range(self.__height):
            for _ in range(self.__width):
                str += "#"
            str += "\n"
        str = str[:-1]
        return str

    def __repr__(self):
        string = ("Rectangle(" + str(self.__width) +
                  ", " + str(self.__height) + ")")
        return string

    def __del__(self):
        print("Bye rectangle...")
