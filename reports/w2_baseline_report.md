# Week 2 Baseline XGBoost Report

## Objective

Evaluate the baseline XGBoost model using engineered spatial features
and interpret predictions through SHAP analysis.

---

## SHAP Interpretation

The SHAP analysis indicates that **dist_city_center** is the most
important feature influencing house price prediction.

Properties located closer to Seattle city center generally receive
higher predicted prices.

Other important contributors include:

- Living area (sqft_living)
- Number of bedrooms
- Distance-based spatial features

---

## Residual Analysis

Residual plots reveal that the baseline model tends to underestimate
high-value luxury and waterfront homes.

Large positive residuals are concentrated among expensive properties,
indicating that additional neighborhood and graph-based spatial context
could further improve prediction accuracy.

---

## Conclusion

The baseline model performs well for average-priced properties,
while premium homes remain more difficult to estimate accurately.

Future work will incorporate graph neural network embeddings and
additional spatial relationships to improve predictive performance.
# Week 2 – XGBoost Baseline & SHAP Analysis

## Objective

Establish a baseline house price prediction model and evaluate how spatial information contributes to prediction accuracy.

---

## Dataset

- Dataset: King County Housing Dataset
- Target Variable: price
- Model: XGBoost Regressor

---

## Feature Engineering

The following engineered features were included:

- House Age
- Distance to Seattle City Center
- Geographic Coordinates (Latitude, Longitude)

---

## Model Evaluation

Evaluation Metrics:

- Mean Absolute Percentage Error (MAPE)
- Residual Analysis

The model predictions were compared with actual sale prices to understand the prediction errors.

---

## SHAP Analysis

SHAP (SHapley Additive exPlanations) was used to interpret feature importance.

Generated Visualizations:

- SHAP Beeswarm Plot
- SHAP Feature Importance Bar Plot

These visualizations explain how each feature contributes to the final prediction.

---

## Residual Analysis

Residual plots were generated to identify systematic prediction errors.

The residual distribution was inspected to determine whether the model consistently overestimates or underestimates specific property categories.

---

## Conclusion

The baseline XGBoost model provides a strong reference for comparison.

The next stage of the project introduces graph-based neighborhood information through KNN graphs and spatial embeddings to improve valuation accuracy.