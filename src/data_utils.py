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
    