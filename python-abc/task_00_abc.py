#!/usr/bin/python3
from abc import ABC, abstractmethod
"""create base class and subclasses"""


class Animal(ABC):
    """an abstract class for Animal"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """a subclass for the Animal Dog"""
    def sound(self):
        return "Bark"


class Cat(Animal):
    """a subclass for the Animal Cat"""
    def sound(self):
        return "Meow"
