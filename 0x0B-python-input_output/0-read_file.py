#!/usr/bin/python3

""" This module reads a file and prints it to stdout """


def read_file(filename=""):
    """ the function takes in a filename as argument
    and will return the contents of the file as output
    """

    with open(filename, 'r', encoding='utf-8') as file:
        line = file.read()
        print(line, end='')
