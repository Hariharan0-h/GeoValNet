# Week 2 – Ablation Study Report

## Objective

Evaluate whether adding spatial features improves house price prediction compared to a baseline tabular model.

## Baseline Model

Features:
- bedrooms
- bathrooms
- sqft_living
- sqft_lot
- floors
- grade
- house_age

Model:
- XGBoost Regressor

Evaluation Metric:
- Mean Absolute Percentage Error (MAPE)

## Spatial Model

Additional Features:
- latitude
- longitude
- distance to Seattle city center

Model:
- XGBoost Regressor

Evaluation Metric:
- Mean Absolute Percentage Error (MAPE)

## Results

| Model | MAPE |
|--------|------|
| Baseline | *(fill your value)* |
| Spatial | *(fill your value)* |

## Observation

The spatial model incorporates geographic information that is not available in a purely tabular model. This experiment establishes the workflow for evaluating the contribution of spatial features and provides a baseline for later additions such as POI distances, KNN graphs, and graph neural networks.

## Next Steps

- Add POI distance features
- Construct KNN graph
- Generate spatial embeddings
- Train GNN / Attention-based valuation model
