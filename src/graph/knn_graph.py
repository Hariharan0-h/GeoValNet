import numpy as np
from math import radians, sin, cos, sqrt, atan2

EARTH_RADIUS_KM = 6371.0


def haversine(lat1, lon1, lat2, lon2):
    """
    Compute the Haversine distance (km) between two latitude/longitude points.
    """

    lat1, lon1, lat2, lon2 = map(
        radians,
        [lat1, lon1, lat2, lon2]
    )

    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = (
        sin(dlat / 2) ** 2
        + cos(lat1)
        * cos(lat2)
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return EARTH_RADIUS_KM * c


def inverse_distance(distance, eps=1e-6):
    """
    Convert distance into an inverse-distance edge weight.
    """

    return 1.0 / (distance + eps)