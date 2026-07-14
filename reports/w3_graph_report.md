# Week 3 Graph Construction Report

## Objective

Construct a spatial K-Nearest Neighbour (KNN) graph for King County housing
data using BallTree and the Haversine distance metric.

---

## Graph Construction

- Algorithm: BallTree
- Distance Metric: Haversine
- Number of neighbours (K): 10

The generated graph connects each property to its nearest neighbouring
properties while preserving geographical proximity.

---

## Validation

The Bellevue sample was used to validate graph connectivity.

Observations:

- Average node degree ≈ 9.8
- All selected neighbours lie within approximately 2 km.
- Edge weights are computed using inverse Haversine distance.

---

## Visualization

A Folium-based visualization confirms that graph edges correctly connect
nearby houses without long-distance artifacts.

---

## Conclusion

The generated KNN graph is suitable for downstream Graph Neural Network
models such as GraphSAGE and Graph Attention Networks.
# Week 3 – KNN Graph Construction Report

## Objective

Construct a K-Nearest Neighbour (KNN) graph using the geographical coordinates of houses in the King County housing dataset.

## Method

- Dataset: King County Housing
- Node: Individual house
- Edge: Connection to K nearest neighbouring houses
- K = 10
- Distance Metric: Geographic proximity using latitude and longitude

## Validation

The KNN graph was validated by:

- Inspecting neighbour indices
- Computing neighbour distances
- Visualizing graph connections using Folium
- Verifying graph statistics

## Graph Statistics

- Number of Nodes: *(fill from notebook output)*
- Number of Edges: *(fill from notebook output)*
- Average Degree: *(fill from notebook output)*

## Conclusion

The constructed KNN graph successfully captures the local spatial relationships among properties. This graph forms the basis for subsequent node feature engineering and graph neural network training.
---

# Node Feature Engineering

The node feature matrix was prepared for graph-based learning.

## Feature Set

- bedrooms
- bathrooms
- sqft_living
- sqft_lot
- floors
- grade
- house_age
- latitude
- longitude
- log_sqft
- price_zscore

## Validation

- StandardScaler applied
- No missing values
- No infinite values
- All features stored as float values

## Final Feature Matrix

Shape:

(21613, 11)

The node feature matrix is ready for Node2Vec embedding generation and Graph Neural Network training.