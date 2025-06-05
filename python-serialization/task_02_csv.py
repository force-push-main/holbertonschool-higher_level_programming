#!/usr/bin/python3
"""i turned myself into a pickle morty!"""
import csv
import json


def convert_csv_to_json(filename):
    cereal_json = []
    try:
        with open(filename, "r") as csv_file:
            data = list(csv.DictReader(csv_file))
        for row in data:
            cereal_json.append(row)
        with open('data.json', "a") as json_file:
            json.dump(cereal_json, json_file)
        return True
    except:
        return False
