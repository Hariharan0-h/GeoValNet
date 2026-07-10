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