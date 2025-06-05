#!/usr/bin/python3
"""i turned myself into a pickle morty!"""
import csv
import json


def convert_csv_to_json(filename):
    try:
        with open(filename, "r") as csv_file:
            data = list(csv.DictReader(csv_file))

        with open('data.json', "w") as json_file:
            json.dump(data, json_file, indent=4)
        return True
    except:
        return False

csv_file = "data.csv"
convert_csv_to_json(csv_file)
print(f"Data from {csv_file} has been converted to data.json")
