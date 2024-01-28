#!/usr/bin/python3
"""The function in this module carries out scalar division for matrices
"""


def matrix_divided(matrix, div):
    """it divides a matrix scalarly by a given number

    Args:
        matrix (list): a matrix of lists
        div (int, float): the number to divide the matrix

    Raises:
        TypeError: matrix must be a list of lists of integers/floats
        TypeError: div must be an integer or float
        TypeError: when each list in the matrix doesn't have the same size

    Returns:
        list: a list of lists of the divided integers/floats
                rounded to two decimal places
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(num, list) for num in matrix) or
            not all((isinstance(mem, int) or isinstance(mem, float))
                    for mem in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    if not all(len(num) == len(matrix[0]) for num in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
