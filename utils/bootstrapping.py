import requests
from os import makedirs
from utils.settings import ORIGINAL_DATA_DIR, ORIGINAL_DATA_FILENAME
# The M2.5+ list in past 30 days via
# http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php
SRC_URL = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_month.csv"


def bootstrap():
    """
    Set up the file folders and fetch the data

    What it expects:
    ----------------
    Nothing

    What it does:
    -------------
    Creates ORIGINAL_DATA_DIR
    Calls fetch_data() to get the data and save it in ORIGINAL_DATA_FILENAME

    What it returns:
    ----------------
    Nothing
    """
    print("Creating directory:", ORIGINAL_DATA_DIR)
    makedirs(ORIGINAL_DATA_DIR, exist_ok=True)
    # get the data
    txt = fetch_official_data()
    with open(ORIGINAL_DATA_FILENAME, 'w') as f:
        f.write(txt)
        print("Wrote", len(txt), 'characters to', ORIGINAL_DATA_FILENAME)


def fetch_official_data():
    """
    What it expects:
    ----------------
    That SRC_URL is a real thing.

    What it does:
    -------------
    Downloads the file at SRC_URL
    Extracts the text from the response

    What it returns:
    ----------------
    The text of the response (string)
    """
    print("Downloading", SRC_URL)
    resp = requests.get(SRC_URL)
    return resp.text
