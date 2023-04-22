#!/usr/bin/python3

""" This module contains a fnc that returns a dictionary
description with simple data structure. """


def class_to_json(obj):
    """ This fnc returns the description about
    the class.
    """
    return obj.__dict__
