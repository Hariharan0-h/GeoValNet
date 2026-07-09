"""
Baseline XGBoost training script.
"""

from builtins import print

import pandas as pd
from sklearn.model_selection import train_test_split


def prepare_data(df):
    """
    Split data into train and validation sets.
    """

    X = df.drop(columns=["price"])
    y = df["price"]

    X_train, X_val, y_train, y_val = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    return X_train, X_val, y_train, y_val


if __name__ == "__main__":

    sample = pd.DataFrame({
        "sqft_living": [1200, 1800, 2500, 3000, 3500],
        "bedrooms": [2, 3, 4, 4, 5],
        "price": [300000, 450000, 650000, 800000, 950000]
    })

    X_train, X_val, y_train, y_val = prepare_data(sample)

    print("Train:", X_train.shape)
    print("Validation:", X_val.shape)