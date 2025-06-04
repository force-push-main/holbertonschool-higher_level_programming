#!/usr/bin/python3
"""function that writes json to file"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file function"""

    with open(filename, "w") as file:
        json.dump(my_obj, file)
