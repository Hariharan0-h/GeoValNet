import networkx as nx
import numpy as np
from node2vec import Node2Vec


def build_graph(indices):
    """
    Build an undirected graph from KNN neighbour indices.
    """

    G = nx.Graph()

    num_nodes = len(indices)

    for i in range(num_nodes):
        G.add_node(i)

        for j in indices[i][1:]:
            G.add_edge(i, int(j))

    return G


def generate_embeddings(indices,
                        dimensions=64,
                        walk_length=30,
                        num_walks=200):

    G = build_graph(indices)

    node2vec = Node2Vec(
        G,
        dimensions=dimensions,
        walk_length=walk_length,
        num_walks=num_walks,
        workers=4
    )

    model = node2vec.fit(
        window=10,
        min_count=1,
        batch_words=4
    )

    embeddings = np.array(
        [
            model.wv[str(i)]
            for i in range(len(indices))
        ]
    )

    return embeddings