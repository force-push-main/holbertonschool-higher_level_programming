#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()

    return {el: a_dictionary[el] for el in a_dictionary}
