#!/usr/bin/python3
"""function adds args to list then writes to file"""
import os
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def add_to_list(*argv):
    """add_to_list function"""

    filename = "add_item.json"
    if not os.path.exists('add_item.json'):
        save_to_json_file([], filename)
    data = load_from_json_file(filename)
    for arg in argv:
        data.append(arg)

    save_to_json_file(data, filename)
