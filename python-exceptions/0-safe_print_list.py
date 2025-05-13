#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    chars_printed = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            chars_printed = chars_printed + 1
        except IndexError:
            print("")
            return chars_printed
    print("")
    return chars_printed
