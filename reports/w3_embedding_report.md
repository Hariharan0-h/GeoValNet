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
---

# Combined Feature Model Evaluation

## Objective

Evaluate whether combining Node2Vec spatial embeddings with tabular housing features improves property price prediction.

## Feature Matrix

The final feature matrix was created by concatenating the engineered tabular features with the learned Node2Vec embeddings.

Current feature matrix shape:

**(21613, 40)**

## Model

- Algorithm: XGBoost Regressor
- Train/Test Split: 80/20
- Random State: 42

## Evaluation

The combined feature model was trained and evaluated on the test set.

Evaluation metrics (MAPE, RMSE and MAE) were recorded in the experiment notebook.

## Observation

The inclusion of graph-based Node2Vec embeddings provides additional spatial context that cannot be captured using only tabular features.

These embeddings encode neighborhood relationships and improve the model's ability to learn location-dependent pricing patterns.

## Conclusion

The hybrid feature representation consisting of tabular attributes and spatial embeddings provides a stronger representation for downstream valuation models and serves as the foundation for Graph Neural Network (GNN) training in the next development stage.
---

# Neighborhood Aggregation Feature Analysis

## Objective

Evaluate whether neighborhood price statistics improve house price prediction.

## Neighbor Features Added

- Mean Neighbor Price
- Standard Deviation of Neighbor Price
- Minimum Neighbor Price
- Maximum Neighbor Price

These statistics were computed from the K-Nearest Neighbor graph.

## Model Performance

| Metric | Value |
|---------|-------|
| MAPE | **12.36%** |
| RMSE | **142321.05** |
| MAE | **69380.24** |

## Observation

Neighborhood aggregation features provide additional information about the local housing market.

The model benefits from knowing the price distribution of nearby houses, improving its ability to estimate property values.

These handcrafted neighborhood statistics serve as an effective intermediate step before adopting graph neural networks.
---

# Motivation for Graph Attention Networks (GAT)

The neighborhood aggregation approach summarizes nearby property prices using handcrafted statistics such as the mean, minimum, maximum and standard deviation.

Although effective, these features treat every neighbor equally and cannot learn complex interactions among neighboring properties.

Graph Attention Networks address this limitation by learning attention weights for each neighboring node.

This enables the model to automatically determine which neighboring properties are most influential for predicting the value of a target house.

Therefore, neighborhood aggregation provides a strong baseline, while GAT offers a more expressive framework for modeling spatial dependencies in real estate valuation.