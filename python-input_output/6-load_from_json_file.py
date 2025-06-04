#!/usr/bin/python3
"""fucntion that loads json from file"""
import json


def load_from_json_file(filename):
    """load_from_json_file function"""

    with open(filename) as file:
        data = json.load(file)
    return data
