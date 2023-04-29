#!/usr/bin/python3

""" this module is about matrix multipication """


def matrix_mul(m_a, m_b):
    """ Args: two lists of integers

    Output: matrix of integers
    """
    if not(isinstance(m_a, list)):
        raise TypeError("m_a must be a list")
    if not(isinstance(m_b, list)):
        raise TypeError("m_b must be a list")
    for ele in m_a:
        if not(isinstance(ele, list)):
            raise TypeError("m_a must be a list of lists")
    for ele in m_b:
        if not(isinstance(ele, list)):
            raise TypeError("m_b must be a list of lists")
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for col in row:
            if not(isinstance(col, (int, float))):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        for col in row:
            if not(isinstance(col, (int, float))):
                raise TypeError("m_b should contain only integers or floats")

    lent_a = len(m_a[0])
    lent_b = len(m_b[0])

    for row in m_a:
        if len(row) != lent_a:
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if len(row) != lent_b:
            raise TypeError("each row of m_b must be of the same size")

    if lent_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    new = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]

    if len(m_a) == 1:
        for row in range(len(m_a)):
            for i in range(len(m_b[0])):
                for col in range(len(m_b)):
                    new[row][i] += m_a[row][col] * m_b[col][i]
    else:
        for row in range(max(len(m_a), len(m_b))):
            for i in range(len(m_b[0])):
                for col in range(min(len(m_b), len(m_a))):
                    if len(m_a) >= len(m_b):
                        new[row][i] += m_a[row][col] * m_b[col][i]
                    else:
                        new[row][i] += m_b[row][col] * m_a[col][i]
    return new
