"""
Geospatial utility functions for GeoValNet.
"""

from builtins import print

import numpy as np


def haversine(lat1, lon1, lat2, lon2):
    """
    Compute the great-circle distance between two points on Earth.

    Parameters
    ----------
    lat1, lon1 : float or ndarray
        Latitude and longitude of first point (degrees).

    lat2, lon2 : float or ndarray
        Latitude and longitude of second point (degrees).

    Returns
    -------
    float or ndarray
        Distance in kilometers.
    """

    R = 6371.0  # Earth's radius in km

    lat1 = np.radians(lat1)
    lon1 = np.radians(lon1)
    lat2 = np.radians(lat2)
    lon2 = np.radians(lon2)

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        np.sin(dlat / 2) ** 2
        + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    )

    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))

    return R * c


if __name__ == "__main__":
    distance = haversine(
        47.6062,
        -122.3321,
        47.6101,
        -122.2015
    )

    print(f"Distance: {distance:.2f} km")