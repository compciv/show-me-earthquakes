from utils.settings import WRANGLED_DATA_FILENAME
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

def haversine(pt_a, pt_b):
    """
    `pt_a` and `pt_b` are tuples with two float numbers each, i.e.
    representing lng/lat pairs:
    (99,100)  (-42, 85)

    The geo distance between the two points is returned in kilometers
    """
    from math import radians, cos, sin, asin, sqrt

    lng_a = radians(pt_a[0])
    lng_b = radians(pt_b[0])
    lat_a = radians(pt_a[0])
    lat_b = radians(pt_b[0])
    # haversine formula
    dlng = lng_b - lng_a
    dlat = lat_b - lat_a
    whatevs = sin(dlat /2 ) ** 2 + cos(lat_a) * cos(lat_b) * sin(dlng / 2) ** 2
    c = 2 * asin(sqrt(whatevs))
    r = 6371 # Radius of earth in kilometers.
    # return the final calculation
    return c * r
