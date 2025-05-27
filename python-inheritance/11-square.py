#!/usr/bin/python3
"""creates subclass of rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """square class inherits rectangle"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
