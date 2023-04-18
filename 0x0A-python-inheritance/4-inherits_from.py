#!/usr/bin/python3
"""Defines a function: inherits_from."""


def inherits_from(obj, a_class):
    """
    Returns True or False if an object is an inherited instance of a class or not.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
