#!/usr/bin/python3
"""subclass of iter function"""


class CountedIterator():
    """class that overrides __next__"""
    def __init__(self, data):
        self.data = data
        self.counter = 0

    def __next__(self):
        if (self.counter >= len(self.data)):
            raise StopIteration
        el = self.data[self.counter]
        self.counter += 1
        return el

    def get_count(self):
        return self.counter
