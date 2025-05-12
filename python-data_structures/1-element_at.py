#!/bin/usr/python3
def element_at(my_list, idx):
    if idx < 0 or idx > len(my_list - 1):
        print("none")
    else:
        print("{:d}".format(my_list[idx]))
