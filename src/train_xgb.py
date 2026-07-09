"""
Baseline XGBoost training script.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error, root_mean_squared_error
from xgboost import XGBRegressor


def prepare_data(df):
    """
    Split data into train and validation sets.
    """
    X = df.drop(columns=["price"])
    y = df["price"]

    X_train, X_val, y_train, y_val = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    return X_train, X_val, y_train, y_val


def train_model(X_train, y_train):
    """
    Train baseline XGBoost model.
    """
    model = XGBRegressor(
        n_estimators=100,
        learning_rate=0.1,
        max_depth=4,
        random_state=42,
    )

    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_val, y_val):
    """
    Evaluate model performance.
    """
    predictions = model.predict(X_val)

    rmse = root_mean_squared_error(y_val, predictions)
    mape = mean_absolute_percentage_error(y_val, predictions)

    print(f"Validation RMSE : {rmse:.2f}")
    print(f"Validation MAPE : {mape:.4f}")


if __name__ == "__main__":

    sample = pd.DataFrame({
        "sqft_living": [1200, 1800, 2500, 3000, 3500],
        "bedrooms": [2, 3, 4, 4, 5],
        "price": [300000, 450000, 650000, 800000, 950000]
    })

    X_train, X_val, y_train, y_val = prepare_data(sample)

    print("Train:", X_train.shape)
    print("Validation:", X_val.shape)

    model = train_model(X_train, y_train)

    print("Model trained successfully.")

    evaluate_model(model, X_val, y_val)