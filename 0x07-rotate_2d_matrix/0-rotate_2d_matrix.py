#!/usr/bin/python3

"""Rotate 2D matrix"""


def rotate_2d_matrix(matrix):
    """rotate given matrix 90 degrees"""

    left, right = 0, len(matrix) - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right

            cache = matrix[top][left + i]
            matrix[top][left + i] = matrix[bottom - i][left]
            matrix[bottom - i][left] = matrix[bottom][right - i]
            matrix[bottom][right - i] = matrix[top + i][right]
            matrix[top + i][right] = cache
        left += 1
        right -= 1
