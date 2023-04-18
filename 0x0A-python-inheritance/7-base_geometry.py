#!/usr/bin/python3
"""Defines a class: BaseGeometry """


class BaseGeometry:
    """A class with public instance methods area and integer_validator."""

    def area(self):
        """Raise exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Checks if a value is an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
