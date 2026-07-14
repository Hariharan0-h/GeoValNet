import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler


def create_node_features(df):
    """
    Create normalized node features for graph learning.
    """

    X = df.copy()

    # Engineered Features
    X["house_age"] = 2015 - X["yr_built"]
    X["log_sqft"] = np.log1p(X["sqft_living"])

    # Standardized target (for analysis only)
    X["price_zscore"] = (
        X["price"] - X["price"].mean()
    ) / X["price"].std()

    features = [
        "bedrooms",
        "bathrooms",
        "sqft_living",
        "sqft_lot",
        "floors",
        "grade",
        "house_age",
        "lat",
        "long",
        "log_sqft",
        "price_zscore"
    ]

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X[features])

    return pd.DataFrame(
        X_scaled,
        columns=features
    )