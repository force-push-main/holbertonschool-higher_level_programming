#!/usr/bin/python3
"""an abstract class for shapes and its subclasses"""
from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = abs(radius)

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width * 2 + self.height * 2


# def has_method(obj, method):
#     attr = getattr(obj, method, None)
#     if callable(attr):
#         return True
#     return False


# def shape_info(obj):
#     if has_method(obj, "area") and has_method(obj, "perimeter"):
#         print(obj.area())
#         print(obj.perimeter())

def shape_info(obj):
    print(f"Area: {obj.area()}")
    print(f"Perimeter: {obj.perimeter()}")
