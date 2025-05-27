#!/usr/bin/python3
"""inherited class rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle inherits BaseGeometry"""
    def __init__(self, width, height):
        if (self.integer_validator('width', width)):
            self.__width = width
        if (self.integer_validator('height', height)):
            self.__height = height
