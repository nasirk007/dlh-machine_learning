#!/usr/bin/env python3
"""Module that filpping a DataFrame."""


def flip_switch(df):
    """Function that do sorting and transpose a DataFrame."""
    df = df.sort_index(ascending=False).T
    return df
