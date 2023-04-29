#!/usr/bin/python3

""" This module is about matrix division """


def matrix_divided(matrix, div):
    """ This function divides all elements in a given matrix

    Args:

    matrix: matrix containing all elements to be divided
    div: divisor of all elements in the matrix

    Output:

    A  new matrix contaiing all divided elements
    """

    new_list = []

    if not(isinstance(div, (int, float))):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix is None or len(matrix) < 2:
        raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")

    for row in matrix:
        new_row = []
        diff = len(row) - len(matrix[0])
        if diff != 0:
            raise TypeError("Each row of the matrix must have the same size")
        if type(row) != list:
            raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
        for col in row:
            if not (isinstance(col, (int, float))):
                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
            else:
                new_ele = "{:.2f}".format((col / div))
                new_row.append(float(new_ele))
        new_list.append(new_row)
    return new_list
