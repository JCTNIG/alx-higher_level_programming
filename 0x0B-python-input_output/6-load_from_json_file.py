#!/usr/bin/python3

""" This module contains a fnc that cretaes an obj from a
json file. """

import json


def load_from_json_file(filename):
    """ this fnc creates an object from a json file """
    with open(filename) as file:
        line = json.load(file)
        return line
