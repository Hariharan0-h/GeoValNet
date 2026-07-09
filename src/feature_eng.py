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
        "yr_renovated": [0, 1998, 2012]
    })

    sample = add_house_age(sample)
    sample = add_renovated_flag(sample)

    print(sample)