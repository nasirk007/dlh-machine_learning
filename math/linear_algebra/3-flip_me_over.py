#!/usr/bin/env python3
"""Module that defines matrix_transpose"""


def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix."""
    transpose = []

    # iterate over columns
    for j in range(len(matrix[0])):
        new_row = []

        # iterate over rows
        for i in range(len(matrix)):
            new_row.append(matrix[i][j])

        # add the constructed row to result
        transpose.append(new_row)

    return transpose
