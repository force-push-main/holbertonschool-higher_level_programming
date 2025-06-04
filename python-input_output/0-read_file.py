#!/usr/bin/python3
"""function that prints file to stdo"""


def read_file(filename=""):
    """the aforementioned file"""
    with open(filename, "r") as file:
        contents = file.read()
        print(contents, end="")
