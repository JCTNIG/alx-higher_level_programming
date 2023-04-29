#!/usr/bin/python3

""" This module prints a square of given size """


def print_square(size):
    """ This function prints out a square

    Args:

    size: must be an integer. it shows the sids of the square

    Output:
    a square of sides size dran using #
    """

    if not(isinstance(size, int)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
