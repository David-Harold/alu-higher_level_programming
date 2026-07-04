#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        matrix_integer = []
        for j in i:
            j = str(j)
            matrix_integer.append(j)
        joined = " ".join(matrix_integer)
        print(joined)

matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

