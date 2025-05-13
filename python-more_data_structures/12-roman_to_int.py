#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    num_conver = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    num_list = list(map(
        lambda c: num_conver[c] if c in num_conver else 0,
        roman_string))
    if 0 in num_list:
        return 0
    value = 0
    subtracted = False
    for i in range(len(num_list)):
        if subtracted:
            subtracted = False
            continue
        if i == len(num_list) - 1:
            value += num_list[i]
        elif (num_list[i] >= num_list[i + 1]):
            value += num_list[i]
        elif (num_list[i] < num_list[i + 1]):
            value += num_list[i + 1] - num_list[i]
            subtracted = True
    return value
