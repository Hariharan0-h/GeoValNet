"""
Feature engineering utilities for GeoValNet.
"""

from builtins import print

import pandas as pd


def add_house_age(df):
    """
    Create house_age feature using reference year 2015.
    """

    df = df.copy()

    df["house_age"] = 2015 - df["yr_built"]

    return df
if __name__ == "__main__":

    sample = pd.DataFrame({
        "yr_built": [1990, 2005, 2010]
    })

    sample = add_house_age(sample)

    print(sample)