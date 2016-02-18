from utils.settings import WRANGLED_DATA_FILENAME
from utils.mapping import haversine
import csv

def filtrate(lng, lat):
    """
    Filters the earthquakes data and returns the 5 records that are closest
     to a given pair of geocoordinates

    What it expects:
    ----------------
    lng (number) - a longitude coordinate
    lat (number) - a latitude coordinate

    That WRANGLED_DATA_FILENAME points to a valid CSV file

    What it does:
    -------------
    - Reads the file at WRANGLED_DATA_FILENAME and parses it as CSV, i.e.
        into a list of dictionaries
    - Creates new list of dicts, in which the records are sorted by the
        haversine function, which calculates the
        distance between the provided lng,lat and
        the 'longitude', 'latitude' of each record


    What it returns:
    ----------------
    A list of 5 dictionaries, each dictionary representing one of the
      5 closest earthquakes
    """

    # put lng and lat into a tuple
    the_pt = (lng, lat)

    # Read the data file
    # being suuuuper verbose here in reading the file
    # and deserializing the CSV...just in case you forgot the
    # step by step procedure...
    # feel free to just do:
    #
    # with open(WRANGLED_DATA_FILENAME, 'r') as f:
    #     quakes = list(csv.DictReader(f.read().splitlines()))

    f = open(WRANGLED_DATA_FILENAME, 'r')
    txt = f.read()
    f.close()
    lines = txt.splitlines()
    csvthingy = csv.DictReader(lines)
    quakes = list(csvthingy)

    # I...hate...how Python does lambdas....
    lambdakey = lambda q: haversine( the_pt, (float(q['longitude']), float(q['latitude'])))
    nearest_quakes = sorted(quakes, key=lambdakey)

    return nearest_quakes[0:5]
