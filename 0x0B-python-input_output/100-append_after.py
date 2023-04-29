#!/usr/bin/python3
"""Defines a function: append_after."""


def append_after(filename="", search_string="", new_string=""):
    """Appends text after each line of a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    texts = ""
    with open(filename) as fn:
        for line in fn:
            texts += line
            if search_string in line:
                texts += new_string
    with open(filename, "w") as wr:
        wr.write(texts)
