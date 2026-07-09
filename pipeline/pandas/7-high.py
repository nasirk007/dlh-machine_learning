#!/usr/bin/env python3
"""Module that sorting values in DataFrame."""


def high(df):
    """Function that sort values in particular column of DataFrame."""
    df = df.sort_values(['High'], descending=True)
    return df
