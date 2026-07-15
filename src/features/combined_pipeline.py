import pandas as pd
import numpy as np


def load_combined_features(csv_path, embedding_path):
    """
    Load tabular features and concatenate them with Node2Vec embeddings.
    """

    # Load housing dataset
    df = pd.read_csv(csv_path)

    # Load embeddings
    embeddings = np.load(embedding_path)

    # Select tabular features
    tabular_features = [
        "bedrooms",
        "bathrooms",
        "sqft_living",
        "sqft_lot",
        "floors",
        "grade",
        "lat",
        "long"
    ]

    X_tabular = df[tabular_features].values

    # Concatenate
    X_combined = np.concatenate(
        [X_tabular, embeddings],
        axis=1
    )

    y = df["price"].values

    return X_combined, y