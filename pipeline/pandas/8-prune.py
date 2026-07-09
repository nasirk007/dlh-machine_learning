#!/usr/bin/env python3
"""Module that remove missing values in DataFrame."""


def prune(df):
    """Function that remove NaN, None, NaT from DataFrame."""
    df = df.dropna(subset=['Close'])
    return df
