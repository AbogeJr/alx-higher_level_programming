#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in range(len(matrix)):
        for i in range(len(matrix[item])):
            print('{:d}'.format(matrix[item][i]), end=' ')
        print()
