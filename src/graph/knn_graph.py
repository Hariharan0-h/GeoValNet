"""
KNN Graph construction using BallTree and Haversine distance.
"""

from builtins import print
from threading import enumerate

import numpy as np
from sklearn.neighbors import BallTree


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
        "long": [-122.33, -122.32, -122.31, -122.30, -122.29]
    })

    distances, neighbors = build_knn_graph(sample, k=5)
    adjacency = build_adjacency_list(sample, k=5)

print("\nAdjacency List")

for node, neighbors in adjacency.items():
    print(node, "->", neighbors)

    print("Neighbor indices")
    print(neighbors)

    print("\nDistances")
    print(distances)