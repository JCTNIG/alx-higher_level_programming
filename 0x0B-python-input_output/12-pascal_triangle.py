#!/usr/bin/python3

""" This module contains a fnc that returns the corresponding 
paschal's triangle of a given number """


def pascal_triangle(n):
    """ This fnc returns the paschal triangle of 
    a given integer
    """
    result = []
    if n <= 0:
        return result
    else:
        for i in range(n):
            lis = []

            lis.append(

