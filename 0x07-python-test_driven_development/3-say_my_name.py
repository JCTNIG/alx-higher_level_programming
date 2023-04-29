#!/usr/bin/python3

""" This module prints the first nd last name
of the user
"""


def say_my_name(first_name, last_name=""):
    """ This function prints the first and last name of a person

    Args:

    first_name: must be string type
    last_name: must be string type

    Output:
    My name is <first name> <last name>
    """

    if not(isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    if not(isinstance(last_name, str)):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
