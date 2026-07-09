"""
Feature engineering utilities for GeoValNet.
"""

from builtins import int, print

import pandas as pd


def add_house_age(df):
    """
    Create house_age feature using reference year 2015.
    """

    df = df.copy()

    df["house_age"] = 2015 - df["yr_built"]

    return df
def add_renovated_flag(df):
    """
    Create renovated binary feature.
    """

    df = df.copy()

    df["renovated"] = (df["yr_renovated"] > 0).astype(int)

    return df
if __name__ == "__main__":

    sample = pd.DataFrame({
    "yr_built": [1990, 2005, 2010],
    "yr_renovated": [0, 1998, 2012],
    "price": [400000, 550000, 620000],
    "sqft_living": [2000, 2500, 3100]
})

sample = add_house_age(sample)
sample = add_renovated_flag(sample)
sample = add_price_per_sqft(sample)

print(sample)

    
def add_price_per_sqft(df):
    """
    Create price_per_sqft feature.
    """

    df = df.copy()

    df["price_per_sqft"] = df["price"] / df["sqft_living"]

    return df