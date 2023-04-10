#!/usr/bin/python3
    """
    Addition function definition.
    """
def add_integer(a, b=98):
    """
    This function adds to numbers of
    either integer or float type only
    and returns the result as integer.
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return int(a + b)
