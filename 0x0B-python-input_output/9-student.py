#!/usr/bin/python3

""" This module contains a class: student """


class Student:
    """ this is a studen class """

    def __init__(self, first_name, last_name, age):
        """ This method instantiates a student class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ This method  retrieves a dictionary representation of a
        Student instance """
        return self.__dict__
