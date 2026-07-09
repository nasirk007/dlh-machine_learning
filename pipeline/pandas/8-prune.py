#!/usr/bin/env python3
"""Module that remove missing values in DataFrame."""


def prune(df):
    """Function that remove NaN, None, NaT from DataFrame."""
        # no panda import needed as df is defined already
    # missing values = NaN, None, NaT, empty cell etc
    # dropena() syntax includes parameters like which drop missing values from:
    # axis = 0 or 1, drop row or col with missing values
    # how = 'any' or 'all', drop any or all missing values
    # subset = limit dropping values from row or col and this
    # dropna with subset will completly remove row or col with missing value
    # means if col Close has NaN while other column in the same row dont have NaN
    # this will remove the row under all column completely
    # to remove specific empty cell or entery, use fillna() method
    # fillna can replace NaN to 0, previous valid value, or mean value of column
    # Syntax = df.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False, ignore_index=False)
    df = df.dropna(subset=['Close'])
    return df
