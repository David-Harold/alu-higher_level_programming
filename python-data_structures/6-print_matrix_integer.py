#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for idx, integer in enumerate(i):
            if i == len(i) -1:
                print("{:d}".format(integer), end = "")
            else:
                print("{:d}".format(integer), end = " ")
        print("{:s}".format(""))
matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

