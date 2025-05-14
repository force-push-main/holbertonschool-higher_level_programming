#!/usr/bin/python3
# 0-add_integer.py
"""simple addition function"""

def add_integer(a, b=98):
    """ returns sum of a and b"""
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)