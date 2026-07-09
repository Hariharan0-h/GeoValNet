"""
Unit tests for data cleaning utilities.
"""

from builtins import print

import pandas as pd
import numpy as np


def remove_outliers_iqr(df, column):
    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return df[(df[column] >= lower) & (df[column] <= upper)].copy()


def test_iqr_outlier_removal():

    df = pd.DataFrame({
        "price": [
            300000,
            350000,
            400000,
            450000,
            500000,
            7000000
        ]
    })

    clean = remove_outliers_iqr(df, "price")

    assert len(clean) == 5


def test_log_price_transform():

    df = pd.DataFrame({
        "price": [300000, 450000, 600000]
    })

    df["log_price"] = np.log1p(df["price"])

    assert df["log_price"].isnull().sum() == 0
    assert (df["log_price"] > 0).all()


if __name__ == "__main__":
    test_iqr_outlier_removal()
    test_log_price_transform()
    print("All tests passed.")