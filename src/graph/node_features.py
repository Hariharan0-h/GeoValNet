import pandas as pd

from sklearn.preprocessing import StandardScaler


def create_node_features(df):
    """
    Create normalized node features for graph learning.
    """

    features = [
        "bedrooms",
        "bathrooms",
        "sqft_living",
        "sqft_lot",
        "floors",
        "grade",
        "lat",
        "long"
    ]

    X = df[features].copy()

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    return pd.DataFrame(
        X_scaled,
        columns=features
    )