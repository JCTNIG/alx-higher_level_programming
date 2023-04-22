#!/usr/bin/python3

""" This modulecontains function that writes a string to a file """


def write_file(filename="", text=""):
    """ This function takes two arguments, the filename and text to be written
    in the file. the output of the program is the number of words written
    to the file.
    """

    with open(filename, 'w') as file:
        file.write(text)
        return len(text)
