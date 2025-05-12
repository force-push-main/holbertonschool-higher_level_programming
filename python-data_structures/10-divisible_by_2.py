#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    is_even = []
    for i in my_list:
        if i % 2 == 0:
            is_even.append(True)
        else:
            is_even.append(False)
    return is_even
