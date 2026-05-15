#!/usr/bin/env python3
"""Module that defines matrix_transpose"""


def matrix_transpose(matrix):
    """Returns the transpose of a 2D matrix"""
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
