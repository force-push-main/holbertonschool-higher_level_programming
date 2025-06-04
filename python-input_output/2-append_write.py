#!/usr/bin/python3
"""function that writes to file and returns len"""


def append_write(filename="", text=""):
    """the append_write function"""

    with open(filename, "a") as file:
        str_len = file.write(text)
        return str_len
