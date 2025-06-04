#!/usr/bin/python3
"""function that writes to file and returns len"""


def write_file(filename="", text=""):
    """aforementioned function"""
    with open(filename, "w") as file:
        str_len = file.write(text)
        return str_len
