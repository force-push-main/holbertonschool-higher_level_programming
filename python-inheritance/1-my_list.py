#!/usr/bin/python3
"""a class that inherits from list and prints it sorted"""


class MyList(list):
    """a class that extends list"""

    def print_sorted(self):
        print(sorted(self))
