#!/usr/bin/python3
# 0-add_integer.py
"""simple addition function"""

def add_integer(a, b=98):
    """ returns sum of a and b"""
    try:
        if not isinstance(a, int) and not isinstance(a, float):
            raise TypeError("a must be an integer")
        if not isinstance(b, int) and not isinstance(b, float):
            raise TypeError("b must be an integer")
        return (int(a) + int(b))
    except TypeError as e:
        print(e)