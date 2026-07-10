#!/usr/bin/env python3
"""Module that set index of DataFrame."""


def index(df):
    """Function that enables timestamp column as  index for DF."""
    # this task and before are kind of object creation in class
    # initial code is already been written under above function
    # let say def index(df) and let me give you the initial code as well
    # import pandas as pd
    # df = pd.DataFrame({'Timestamp': [data1, date2, date3],'Value': [Val1, Val2, Val3]})
    # see no of different column per checker file in 10-main.py
    # Print(df) will result in first column with index as default,
    # 2nd is timestamp and 3rd is value while below code line will 
    # just replace first column of index to timestamp
    df = df.set_index('Timestamp')
    return df
