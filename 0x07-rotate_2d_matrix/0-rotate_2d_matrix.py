#!/usr/bin/python3
"""
Given an n x n 2D matrix, rotate it 90 degrees clockwise
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.

Solution:
in solving this, I used a reverse and eventually a transpose
"""


def rotate_2d_matrix(matrix):
    """
    rotates a 2d matrix by 90 degrees in place
    """
    matrix[:] = matrix[::-1]  # reverse by slicing
    for r_i in range(len(matrix)):
        for c_i in range(r_i):
            matrix[r_i][c_i], matrix[c_i][r_i] =\
                matrix[c_i][r_i], matrix[r_i][c_i]
