#!/usr/bin/python3
"""class that returns dict of self"""


class Student():
    """student class"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            new_dict = {key: value for key,
                        value in self.__dict__.items() if key in attrs}
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        class_dict = self.__dict__
        for key in json.items():
            class_dict[key] = json[key]
