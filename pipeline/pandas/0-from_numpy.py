#!/usr/bin/env python3
import pandas as pd


def from_numpy(array):
    # Convert a numpy.ndarray to a pandas.DataFrame
    # after covering, lable each column with a letter starting from A to Z (26)
    # by default, row and column labels are assigned as 0, 1, 2,...
    # DataFrame represent column and row and is 2D so array must be 2D
    # no need to create numpy array as it already passed as argument
    # no need to check as array is 2D as it is already passed as argument
    # shape is a tuple of (rows, columns) so we can use array.shape[1]
    # to get the number of columns in range
    # we use chr to convert index (0, 1, 2,...) to ASCII code
    # Standard Syntax: pd.DataFrame(data, index, columns, dtype, copy)
    # data is mandatory parameter while rest are optional parameters
    lable = []
    for i in range(array.shape[1]):
        lable.append(chr(65 + i))
    df = pd.DataFrame(array, columns=lable)
    return df
