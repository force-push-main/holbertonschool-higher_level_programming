#!/usr/bin/python3
"""empty class called base geometry"""


class BaseGeometry:
    """class with public instance method"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if (not isinstance(value, int) or
                type(value) is not int):
            msg = f"{name} must be an integer"
            raise TypeError(msg)
        if value <= 0:
            msg = f"{name} must be greater than 0"
            raise ValueError(msg)
