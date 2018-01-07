"""
You are given a NxM matrix of integer numbers.

Implement a function, called sum_matrix(m) that returns the sum of all numbers in the matrix.

The matrix will be represented as nested lists in Python.
"""


def sum_matrix(matrix):
    return sum([element for row in matrix for element in row])


if __name__ == '__main__':
    print('***Sum of all elements in matrix***')
    print(sum_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(sum_matrix([[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(sum_matrix([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]))
