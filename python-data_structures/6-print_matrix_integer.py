#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for idx, integer in enumerate(i):
            if idx == len(i) - 1:
                print("{:d}".format(integer), end="")
            else:
                print("{:d}".format(integer), end=" ")
        print()
