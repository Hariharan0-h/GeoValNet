import pandas as pd


def add_spatial_features(df):

    df = df.copy()

    if "dist_to_school" not in df.columns:
        df["dist_to_school"] = 0.0

    if "dist_to_hospital" not in df.columns:
        df["dist_to_hospital"] = 0.0

    return df


if __name__ == "__main__":

    sample = pd.DataFrame({
        "price":[100000,200000]
    })

    sample = add_spatial_features(sample)

    print(sample)
    