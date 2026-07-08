"""
Unit tests for geo_utils.py
"""

from builtins import print, round
import sys
from pathlib import Path

# Add src directory to Python path
sys.path.append(str(Path(__file__).resolve().parents[1] / "src"))

from geo_utils import haversine


def test_haversine_seattle_bellevue():
    """
    Seattle Downtown → Bellevue distance
    Expected ≈ 11.5 km
    """

    distance = haversine(
        47.6062,
        -122.3321,
        47.6101,
        -122.2015
    )

    assert abs(distance - 11.5) < 1.0


def test_same_location():
    """Distance between identical coordinates should be zero."""

    distance = haversine(
        47.6062,
        -122.3321,
        47.6062,
        -122.3321
    )

    assert round(distance, 6) == 0.0


if __name__ == "__main__":
    test_haversine_seattle_bellevue()
    test_same_location()
    print("All tests passed!")