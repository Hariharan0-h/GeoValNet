import numpy as np


def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Compute the Haversine distance (in kilometers)
    between two latitude/longitude points.
    """

    R = 6371.0

    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(lat1)
        * np.cos(lat2)
        * np.sin(dlon / 2) ** 2
    )

    c = 2 * np.arcsin(np.sqrt(a))

    return R * c


def nearest_distance(lat, lon, poi_locations):
    """
    Return the minimum distance from a property
    to a list of POI locations.
    """

    distances = [
        haversine_distance(lat, lon, poi_lat, poi_lon)
        for poi_lat, poi_lon in poi_locations
    ]

    return min(distances)


def compute_poi_features(df, poi_data):
    """
    Compute distance features for multiple POI categories.

    Parameters
    ----------
    df : pandas.DataFrame
        Property dataset containing 'lat' and 'long'.

    poi_data : dict
        Dictionary containing POI categories and coordinates.

    Returns
    -------
    pandas.DataFrame
        DataFrame with additional POI distance features.
    """

    feature_map = {
        "parks": "dist_to_nearest_park",
        "transit": "dist_to_transit_stop",
        "schools": "dist_to_nearest_school",
        "hospitals": "dist_to_nearest_hospital",
        "shopping": "dist_to_nearest_shopping_center",
    }

    result = df.copy()

    for category, feature_name in feature_map.items():

        if category not in poi_data:
            continue

        result[feature_name] = result.apply(
            lambda row: nearest_distance(
                row["lat"],
                row["long"],
                poi_data[category],
            ),
            axis=1,
        )

    return result