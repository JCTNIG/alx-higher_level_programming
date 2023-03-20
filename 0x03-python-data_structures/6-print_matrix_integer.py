#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        print(" ".join("{}".format(i) for i in x))
