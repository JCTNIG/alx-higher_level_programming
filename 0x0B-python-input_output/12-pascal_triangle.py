#!/usr/bin/python3

#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    while len(triangle) != n:
        trian = triangle[-1]
        tmpr = [1]
        for i in range(len(trian) - 1):
            tmpr.append(trian[i] + trian[i + 1])
        tmpr.append(1)
        triangle.append(tmpr)
    return triangle
