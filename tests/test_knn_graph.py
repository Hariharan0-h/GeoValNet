import pandas as pd

from src.graph.knn_graph import build_adjacency_list


def test_graph_node_count():
    df = pd.DataFrame({
        "lat": [47.60, 47.61, 47.62, 47.63, 47.64],
        "long": [-122.33, -122.32, -122.31, -122.30, -122.29]
    })

    for k in [5, 10, 15]:
        graph = build_adjacency_list(df, k=min(k, len(df) - 1))
        assert len(graph) == len(df)