#!/usr/bin/python3
"""Creates a class of objects"""


class Student:
    """A class student"""

    def __init__(self, first_name, last_name, age):
        """initialization of class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrives dictionary representation of students"""
        return self.__dict__
