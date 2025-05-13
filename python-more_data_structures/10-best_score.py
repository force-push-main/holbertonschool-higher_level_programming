#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score = 0
    for key in a_dictionary:
        if a_dictionary[key] > max_score:
            max_score = a_dictionary[key]
            name = key
    return name
