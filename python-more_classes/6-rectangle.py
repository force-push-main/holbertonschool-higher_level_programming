#!/usr/bin/python3

"""a function that creates a class called rectangle"""


class Rectangle:
    """an class for a rectangle object"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1
        self.print_symbol = Rectangle.print_symbol

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
        string = ""
        for _ in range(self.__height):
            for _ in range(self.__width):
                string += str(self.print_symbol)
            string += "\n"
        string = string[:-1]
        return string

    def __repr__(self):
        string = ("Rectangle(" + str(self.__width) +
                  ", " + str(self.__height) + ")")
        return string

    def __del__(self):
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")
