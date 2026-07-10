"""
KNN graph construction using BallTree and Haversine distance.
"""

import numpy as np
from sklearn.neighbors import BallTree


def build_adjacency_list(df, k=10):
    """
    Build adjacency list using BallTree with Haversine metric.
    """

    coords = np.radians(df[["lat", "long"]])

    tree = BallTree(coords, metric="haversine")

    distances, indices = tree.query(coords, k=k)

    adjacency = {}

    for i in range(len(df)):
        adjacency[i] = indices[i].tolist()

    return adjacency, distances


def compute_edge_weights(distances):
    """
    Compute inverse-distance edge weights.
    """

    distances_km = distances * 6371

    weights = 1 / (distances_km + 1e-6)

    return weights


if __name__ == "__main__":

    import pandas as pd

    sample = pd.DataFrame({
        "lat": [
            47.6101,
            47.6112,
            47.6123,
            47.6135,
            47.6140
        ],
        "long": [
            -122.2015,
            -122.2021,
            -122.2030,
            -122.2040,
            -122.2051
        ]
    })

    adjacency, distances = build_adjacency_list(sample, k=3)

    weights = compute_edge_weights(distances)

    print("Adjacency List")
    print(adjacency)

    print("\nEdge Weights")
    print(weights)