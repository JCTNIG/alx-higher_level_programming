#!/usr/bin/python3
"""Defines a function: is_same_class."""


def is_same_class(obj, a_class):
    """
    Returns True or False if an object is exactly an instance of a given class not
    """
    if type(obj) == a_class:
        return True
    return False
