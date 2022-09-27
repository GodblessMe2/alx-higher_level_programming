#!/usr/bin/python3
"""Contains class of Student"""


class Student:
    """A representation of a student"""
    def __init__(self, first_name, last_name, age):
        """
        Initializing the student class
        Args:
           first_name (str): first_name of the new student
           last_name (str): last_name of the new student
           age (int): age of the new student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a
           Student
        Args:
           attr (lists): the attributes to represent
        """
        if (type(attrs) == list and
            all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student.
        Args:
            json (dict): The key/value pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(self, k, v)
