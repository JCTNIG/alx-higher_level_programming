#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a_dict = {}
    for key, value in a_dictionary.items():
        a_dict[key] = value * 2
    return a_dict
