#!/usr/bin/python3

""" this module uses numpy for matrix multiplication """


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    the input is a list of list which will be converted
    to a numpy array
    """

    m_a = np.array(m_a)
    m_b = np.array(m_b)

    return np.dot(m_a, m_b)
