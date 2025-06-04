#!/usr/bin/python3
"""fucntion that loads json from file"""
import json


def load_from_json_file(filename):
    """load_from_json_file function"""

    with open(filename, "r"):
        data = json.load(filename)
    return data
