#!/usr/bin/python3

""" This module contains a function that writes an
object to a text file """

import json


def save_to_json_file(my_obj, filename):
    """ This fnc takes in two args, an object to
    write in a file """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
