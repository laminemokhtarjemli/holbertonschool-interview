#!/usr/bin/python3
""" Rotate 2D Matrix"""


def rotate_2d_matrix(matrix):
    """ Function to rotate a 2D matrix """

    if len(matrix) < 2:
        return

    rows = len(matrix)

    for i in range(0, int(rows / 2)):
        for j in range(i, rows - i - 1):
            element = matrix[i][j]
            matrix[i][j] = matrix[rows - j - 1][i]
            matrix[rows - j - 1][i] = matrix[rows - i - 1][rows - j - 1]
            matrix[rows - i - 1][rows - j - 1] = matrix[j][rows - i - 1]
            matrix[j][rows - i - 1] = element

    return