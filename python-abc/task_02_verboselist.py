#!/usr/bin/python3
"""extended list class"""


class VerboseList(list):
    """class extends list class"""

    def append(self, el):
        super().append(el)
        print(f"Added [{el}] to the list.")

    def extend(self, iterable):
        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items")

    def remove(self, el):
        super().remove(el)
        print(f"Removed [{el}] from the list.")

    def pop(self, index=-1):
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)
