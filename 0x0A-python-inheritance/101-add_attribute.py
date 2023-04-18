#!/usr/bin/python3
"""Defines a function: add_attribute."""


def add_attribute(obj, att, value):
    """
    Declares function: add_attribute,
    Add a new attribute to an object if possible.
    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
