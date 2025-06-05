#!/usr/bin/python3
"""im pickle riiiiiick!!!!!"""
import pickle
import os


class CustomObject:
    def __init__(self, name=None, age=None, is_student=None):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        # if not os.path.isfile(filename):
        #     return None
        try:
            with open(filename, 'rb') as file:
                data = pickle.load(file)
                return data
        except:
            return None
