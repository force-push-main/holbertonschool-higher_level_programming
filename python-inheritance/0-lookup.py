#!/usr/bin/python3
"""
a function that returns list of all attributes and methods
available to a object
"""


def lookup(obj):
    """the aforementioned function"""
    return dir(obj)
