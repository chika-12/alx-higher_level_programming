#!/usr/bin/python3
"""
python code for dividing a matrix

"""


def matrix_divided(matrix, div):
    """
    This codes divides elements of a matrix by div

    """
    if not(isinstance(matrix, list) or matrix == [] or
            not(isinstance(row, list) for row in matrix) or
            not ((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in matrix for num in row])):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError ("div must be a number")
    if div < 0:
        raise ZeroDivisionError("division by zero")
    big = []
    for colum in matrix:
        small = []
        for row in colum:
            val = round(row / div, 2)
            small.append(val)
        big.append(small)
    return big
