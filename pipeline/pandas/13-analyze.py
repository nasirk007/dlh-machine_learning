#!/usr/bin/env python3
"""Module that show stats of DataFrame."""


def analyze(df):
    """Function that show descriptive state of DataFrames."""
    # df.describe() provide normally work on numeric columns but for 
    # mixed (numeric and categorial data in columns), we should use
    # df.mixed_describe()
    # parameters for this method could be include, exclude, 
    # show only specifc stat like mean, variance, min/max, percentile etc 
    # include='all', means give stat for both numeric and categorial data in column
    # include='object' or 'number' or 'datetime' 
    # object means give state for column with strings in table
    # exclude='object' or 'number' or 'datetime' or 'spec_col' 
    # give only percentile stats like percentile=[0.1, 0.5, 0.9]
    # number: Covers int64, float64, etc.
    # datetime: Covers datetime64[ns], Timestamp, etc.
    # object: Covers strings and mixed types.
    # another way df = df.describe(include='number')
    # another way df = df.drop(columns='Timestamp').describe()
    # another way isto loop like 
    # stat_col = []
    # for c in df.columns:
    #   if c != 'Timestamp':
    #      stat_col.append(c)
    # df['stat_col'].describe() 
    df = df.describe(exclude='datetime')
    return df
