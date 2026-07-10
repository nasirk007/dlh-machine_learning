#!/usr/bin/env python3
"""Module that fill missing values in pandas DataFrame."""
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
    # df.drop(labels=None, axis=0, index=None, columns=None, inplace=False, errors='raise')
    # df.fillna(value=None, method=None, axis=0, inplace=False, limit=None)
    # backward fill = df.bfill() and forward fill = df.ffill instead of 
    # fillna(method='ffill') or fillna(method='bfill')


def fill(df):
    """Function that fill empty cells in row and column of DF."""
    # remove weighted price col at all and 1 represent col index
    df = df.drop(['Weighted_Price'], axis=1)

    # doing forward fill for close column
    df['Close'] = df['Close'].ffill()

    # it was not possible to fill each column with close value in 
    # one go like, see below 
    # df[['High', 'Low', 'Open']] = df[['High', 'Low', 'Open']].fillna(df['Close'])
    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])

    # its possible to fill multiple column with NaN cell 
    # with 0 in one go, see below 
    df[['Volume_(BTC)', 'Volume_(Currency)']] = df[[
        'Volume_(BTC)', 'Volume_(Currency)']].fillna(0)
    return df
