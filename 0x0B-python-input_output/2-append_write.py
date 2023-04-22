#!/usr/bin/python3

""" This module contains function that appends a text to a file """


def append_write(filename="", text=""):
    """ This function appends a text to
    a file. it will return the number of
    characters added to the file.
    """
    with open(filename, 'a') as file:
        file.write(text)
        return len(text)
