#!/usr/bin/env python3
"""Module that concate two objects referred as DataFrame."""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """Task that concate two DataFrames."""
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2.iloc[:1417411920]
    df3 = [df1, df2]
    df = pd.concat(df3, keys=['bitstamp', 'coinbase'])
    return df
