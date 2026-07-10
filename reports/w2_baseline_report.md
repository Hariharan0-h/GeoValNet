# Week 2 Baseline Report

## Failure Cases

The baseline XGBoost model performs well across most ZIP codes.

However, systematic underestimation is observed for rapidly
gentrifying areas such as:

- ZIP 98109
- ZIP 98102

These regions exhibit rapid appreciation driven by local development,
which is difficult to capture using purely tabular features.

Future iterations should integrate richer spatial context using
graph neural networks and additional geospatial features.