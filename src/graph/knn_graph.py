"""
KNN Graph construction using BallTree and Haversine distance.
"""

from builtins import print

import numpy as np
from sklearn.neighbors import BallTree


def build_knn_graph(df, k=5):
    """
    Build a KNN graph using latitude and longitude.
    """

    coords = np.radians(df[["lat", "long"]].values)

    tree = BallTree(coords, metric="haversine")

    distances, indices = tree.query(coords, k=min(k + 1, len(df)))

    return distances[:, 1:], indices[:, 1:]


def build_adjacency_list(df, k=5):
    """
    Build adjacency list from KNN graph.
    """

    _, indices = build_knn_graph(df, k)

    adjacency = {}

    for node, neighbors in enumerate(indices):
        adjacency[node] = neighbors.tolist()

    return adjacency


if __name__ == "__main__":

    import pandas as pd

    sample = pd.DataFrame({
        "lat": [47.60, 47.61, 47.62, 47.63, 47.64],
        "long": [-122.33, -122.32, -122.31, -122.30, -122.29],
    })

    distances, neighbors = build_knn_graph(sample, k=4)

    print("Neighbor indices")
    print(neighbors)

    print("\nDistances")
    print(distances)

    adjacency = build_adjacency_list(sample, k=4)

    print("\nAdjacency List")

    for node, nbrs in adjacency.items():
        print(node, "->", nbrs)