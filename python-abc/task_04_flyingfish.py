#!/usr/bin/python3
"""multiple inheritance"""


class Fish():
    @staticmethod
    def swim():
        print("The fish is swimming")

    @staticmethod
    def habitat():
        print("The fish lives in water")


class Bird():
    @staticmethod
    def fly():
        print("The bird is flying")

    @staticmethod
    def habitat():
        print("The bird lives in the sky")


class FlyingFish(Bird, Fish):
    @staticmethod
    def fly():
        print("The flying fish is soaring!")

    @staticmethod
    def swim():
        print("The flying fish is swimming!")

    @staticmethod
    def habitat():
        print("The flying fish lives both in water and the sky!")
