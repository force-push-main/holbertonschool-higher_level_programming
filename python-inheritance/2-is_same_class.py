#!/usr/bin/python3
"""checks whether object is instance of different class"""


def is_same_class(obj, a_class):
    """function checks if obj is exactly instance of a_class"""
    return type(obj) is a_class
