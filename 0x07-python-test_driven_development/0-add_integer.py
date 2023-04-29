#!/usr/bin/python3

""" This module is about add_integer function """


def add_integer(a, b=98):
    """ This function adds two integers.
    Args:
    a : positional argument
    b : keyword argument
    Output:
    The function will return the sum of a and b
    """
    if not(isinstance(a, (int, float))):
        raise TypeError("a must be an integer")
    if not(isinstance(b, (int, float))):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
