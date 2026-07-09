#!/usr/bin/env python3
"""Module that fill missing values in pandas DataFrame."""


def fill(df):
    """Function that fill empty cells in row and column of DF."""
    df = df.drop(['Weighted_Price'], axis=1)
    df['Close'] = df['Close'].ffill()
    df['High'] = df['High'].fillna(df['Close'])
    df['Low'] = df['Low'].fillna(df['Close'])
    df['Open'] = df['Open'].fillna(df['Close'])
    df[['Volume_(BTC)', 'Volume_(Currency)']] = df[[
        'Volume_(BTC)', 'Volume_(Currency)']].fillna(0)
    return df
