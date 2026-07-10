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