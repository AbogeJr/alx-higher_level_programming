#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for arr in matrix:
        new_arr = []
        for i in arr:
            new_arr.append(i ** 2)
        new_matrix.append(new_arr)

    return new_matrix
