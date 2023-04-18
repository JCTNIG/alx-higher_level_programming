#!/usr/bin/python3
""" returns a list of all attributes and methods of an object """


def lookup(obj):
    """Return a list of an object's available attributes and instances."""
    return (dir(obj))
