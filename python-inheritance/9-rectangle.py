#!/usr/bin/python3
"""inherited class rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits BaseGeometry"""
    def __init__(self, width, height):
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
