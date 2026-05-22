#!/usr/bin/env python3
def determinant(matrix):
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a list of lists")
    if matrix[[]]:
        return 1
    for row in matrix:
        if len(row) != len(matrix):
            raise TypeError("matrix must be a square matrix")
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        return a*d - b*c
    det = 0

    for j in range(len(matrix)):
        minor = []
        for r in range(1, len(matrix)):
            row = []
            for c in range(len(matrix)):
                if c != j:
                    row.append(matrix[r][c])
            minor.append(row)
        det += ((-1) ** j) * matrix[0][j] * determinant(minor)
    return det