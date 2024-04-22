#!/usr/bin/python3
"""
python code for dividing a matrix

"""


def matrix_divided(matrix, div):
    """
    This codes divides elements of a matrix by div

    """
    big = []
    for colum in matrix:
        small = []
        for row in colum:
            val = round(row / div, 2)
            small.append(val)
        big.append(small)
    return big
