#!/usr/bin/python3
"""Defines a class: MyInt"""


class MyInt(int):
    """A rebel class with reversed int
    operators == and !=
    """

    def __eq__(self, value):
        """ replaces '==' opeartor with '!=' behavior."""
        return self.real != value

    def __ne__(self, value):
        """ replaces '!=' operator with '==' behavior."""
        return self.real == value
