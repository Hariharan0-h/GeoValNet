import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


def build_pipeline():

    return Pipeline([
        ("scaler",StandardScaler())
    ])


def add_spatial_features(df):

    df=df.copy()

    if "dist_to_school" not in df.columns:
        df["dist_to_school"]=0

    if "dist_to_hospital" not in df.columns:
        df["dist_to_hospital"]=0

    return df


if __name__=="__main__":

    sample=pd.DataFrame({
        "dist_to_school":[1.2,2.4],
        "dist_to_hospital":[3.1,4.6]
    })

    pipeline=build_pipeline()

    transformed=pipeline.fit_transform(sample)

    print(transformed)