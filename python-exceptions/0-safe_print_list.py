#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    chars_printed = 0
    for num in my_list:
        try:
            print("{}".format(num), end="")
            chars_printed = chars_printed + 1
        except:
            print("\n")
            return chars_printed
    print("\n")
    return chars_printed
