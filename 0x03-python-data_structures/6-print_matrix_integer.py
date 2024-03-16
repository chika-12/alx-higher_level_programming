#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    num = 0
    for row in matrix:
        for val in row:
            print("{:d}".format(val), end="")
            if num < len(row) - 1:
                print(" ", end="")
            num += 1
        num = 0
        print()
