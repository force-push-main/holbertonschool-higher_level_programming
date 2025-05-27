#!/usr/bin/python3
"""function to check if obj inherits from class"""


def inherits_from(obj, a_class):
    """aforementioned function"""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
