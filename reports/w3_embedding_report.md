# Week 3 – Node2Vec Embedding Analysis

## Objective

Evaluate the quality of Node2Vec embeddings generated from the K-Nearest Neighbour (KNN) graph constructed using the King County Housing dataset.

---

## Embedding Configuration

- Graph Type: KNN Graph
- Number of Neighbours (K): 10
- Embedding Dimension: 64
- Embedding Algorithm: Node2Vec

---

## UMAP Visualization

The 64-dimensional embeddings were projected to two dimensions using UMAP for visual inspection.

The visualization indicates that houses with similar spatial relationships tend to form clusters in the embedding space.

---

## Cosine Similarity Analysis

Cosine similarity was computed on a representative sample of Node2Vec embeddings.

Observed Average Cosine Similarity:

**0.3725**

The similarity matrix confirms that the learned embeddings preserve meaningful spatial relationships while distinguishing geographically different properties.

---

## Conclusion

The generated Node2Vec embeddings successfully encode neighborhood structure and are suitable for downstream machine learning tasks such as graph-based valuation and feature fusion with XGBoost.