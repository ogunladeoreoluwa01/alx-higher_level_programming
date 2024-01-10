#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    r = []
    for member in matrix:
        r.append(list(map(lambda x: x ** 2, member)))
    return r
