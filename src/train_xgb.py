import pandas as pd
import numpy as np
from xgboost import XGBRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import (
    mean_absolute_percentage_error,
    root_mean_squared_error,
)


sample = pd.DataFrame({
    "sqft_living": [1200,1800,2500,3000,3500,1600,2200,2800,3200,4000],
    "bedrooms":[2,3,4,4,5,3,3,4,5,5],
    "price":[300000,450000,650000,800000,950000,
             380000,520000,710000,860000,1100000]
})

X = sample.drop(columns=["price"])
y = sample["price"]

kf = KFold(
    n_splits=5,
    shuffle=True,
    random_state=42,
)

model = XGBRegressor(
    n_estimators=100,
    learning_rate=0.1,
    max_depth=4,
    random_state=42,
)

mape_scores = []
rmse_scores = []

fold = 1

for train_idx, test_idx in kf.split(X):

    X_train = X.iloc[train_idx]
    X_test = X.iloc[test_idx]

    y_train = y.iloc[train_idx]
    y_test = y.iloc[test_idx]

    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    mape = mean_absolute_percentage_error(y_test, pred)
    rmse = root_mean_squared_error(y_test, pred)

    mape_scores.append(mape)
    rmse_scores.append(rmse)

    print(
        f"Fold {fold}: "
        f"MAPE={mape:.4f} "
        f"RMSE={rmse:.2f}"
    )

    fold += 1

print("\nAverage Results")

print("MAPE:", np.mean(mape_scores))
print("RMSE:", np.mean(rmse_scores))