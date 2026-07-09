"""
Download utility for the King County Housing dataset.

This is a placeholder implementation. Replace the URL or Kaggle
download logic with the actual dataset source when available.
"""

from builtins import Exception, print
from pathlib import Path
import urllib.request


DATA_DIR = Path("data/raw")
DATA_DIR.mkdir(parents=True, exist_ok=True)

DATA_URL = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"

OUTPUT_FILE = DATA_DIR / "housing.csv"


def download_dataset():
    try:
        urllib.request.urlretrieve(DATA_URL, OUTPUT_FILE)
        print(f"Dataset downloaded successfully to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Download failed: {e}")


if __name__ == "__main__":
    download_dataset()