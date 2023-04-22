#!/usr/bin/python3

""" This module contains a function that returns an
object (Python data structure) represented by a
JSON string """

import json


def from_json_string(my_str):
    """ this fnc takes in an arg and returns
    a JSON object """
    return json.loads(my_str)
