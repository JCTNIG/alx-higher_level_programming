#!/usr/bin/python3

""" This module contains a class: student """


class Student:
    """ this is a studen class """

    def __init__(self, first_name, last_name, age):
        """ This method instantiates a student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ This method  retrieves a dictionary representation of a
        Student instance """
        if isinstance(attrs, list) and\
           all(isinstance(ele, str) for ele in attrs):
            return {k: v for k, v in vars(self).items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """ This method replaces all attributes of the Student instance
        """
        for key, value in json.items():
            setattr(self, key, value)
