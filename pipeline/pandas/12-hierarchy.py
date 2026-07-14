#!/usr/bin/env python3
"""Module that use hierarchical indexing for two DataFrame."""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Task that apply hierarchical indexing over DataFrames."""
    df1 = index(df1)
    df2 = index(df2)
    df2 = df2.loc[:1417411920]
    df = pd.concat([df2, df1], keys=['bitstamp', 'coinbase'])
        
    return df
