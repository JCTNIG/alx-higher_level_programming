#!/usr/bin/python3

""" This module contains function that
indents a text after certain characyers
"""


def text_indentation(text):
    """ This function prints a text with 2 new lines after
    each of the specified characters.

    Args:
    text: must be a string data type.

    Output:
    line indented texts
    """

    if not(isinstance(text, str)):
        raise TypeError("text must be a string")

    for letter in text:
        if letter in (".", "?", ":"):
            print(letter.rstrip(), "\n\n", end='')
        else:
            print(letter.rstrip(), end='')
