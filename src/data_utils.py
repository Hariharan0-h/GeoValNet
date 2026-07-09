"""
Data utility functions for GeoValNet.
"""

from pathlib import Path
import geopandas as gpd


def export_cleaned_data(gdf, output_path="data/processed/kc_clean.gpkg"):
    """
    Export cleaned GeoDataFrame to GeoPackage format.
    """

    output_path = Path(output_path)

    output_path.parent.mkdir(parents=True, exist_ok=True)

    gdf.to_file(output_path, driver="GPKG")

    print(f"Dataset exported to: {output_path}")


def validate_bbox(gdf, min_lat, max_lat, min_lon, max_lon):
    """
    Validate that all points lie within the specified bounding box.
    """

    outside = gdf[
        (gdf.geometry.y < min_lat)
        | (gdf.geometry.y > max_lat)
        | (gdf.geometry.x < min_lon)
        | (gdf.geometry.x > max_lon)
    ]

    if len(outside) > 0:
        raise ValueError(
            f"{len(outside)} point(s) found outside bounding box."
        )

    print("Bounding box validation passed.")

    return True


if __name__ == "__main__":

    sample = gpd.GeoDataFrame(
        {
            "price": [300000, 450000],
            "geometry": gpd.points_from_xy(
                [-122.3321, -122.2015],
                [47.6062, 47.6101],
            ),
        },
        crs="EPSG:4326",
    )

    export_cleaned_data(sample)

    validate_bbox(
        sample,
        min_lat=47.0,
        max_lat=48.0,
        min_lon=-123.0,
        max_lon=-121.0,
    )