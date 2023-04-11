#!/usr/bin/python3
"""defines a matrix dividing function: matrix_divided"""


def matrix_divided(matrix, div):
    """ This function divides all elements in a given matrix
    Args: The matrix list and the division number
    Output: A new matrix list rounded to 2 decimals
    """
    if matrix is None or len(matrix) < 2:
        raise TypeError("matrix must be a matrix (list of lists)\
                           of integers/floats")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)\
                      of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []

    for row in matrix:
        row_size = len(row) - len(matrix[0])
        if row_size != 0:
            raise TypeError("Each row of the matrix must have the same size")
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix\
                       (list of lists) of integers/floats")

        new_row = []
        for col in row:
            if not isinstance(col, (int, float)):
                raise TypeError("matrix must be a matrix\
                  (list of lists) of integers/floats")
            x = "{:.2f}".format(col / div)
            new_row.append(float(x))
        new_list.append(new_row)
    return new_list
