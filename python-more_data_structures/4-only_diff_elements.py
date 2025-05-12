#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    return list(filter(lambda el: el not in set_2, set_1))
