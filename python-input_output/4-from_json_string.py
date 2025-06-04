#!/usr/bin/python3
"""function that converts json to object"""
import json


def from_json_string(my_str):
    """from_json_string function"""

    return json.loads(my_str)
