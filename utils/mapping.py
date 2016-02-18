from urllib.parse import urlencode

GOOGLEMAP_ENDPOINT_URL = 'https://maps.googleapis.com/maps/api/staticmap'


def google_map_marker(location, label=None, color="red"):
    m = []
    if label:
        m.append("label:" + label)
    if color:
        m.append("color:" + color)
    # finally, append the location
    m.append(location)
    # finally, finally, join each thing together with a pipe
    return '|'.join(m)


def google_static_map_url(markers, size="300x300", maptype="terrain", zoom="", center=""):
    """
    markers can either be a string,
        e.g. "Ohio" or "34,-78.9" (lat,lng) or "label:X|color:green|New York"
        or a collection of such strings
    """
    map_params = {"size": size, "zoom": zoom, "center": center,
                  "maptype": maptype, "markers": markers}
    query_string = urlencode(map_params, doseq=True)
    return GOOGLEMAP_ENDPOINT_URL + '?' + query_string



def haversine(pt_a, pt_b):
    """
    `pt_a` and `pt_b` are tuples with two float numbers each, i.e.
    representing lng/lat pairs:
    (99,100)  (-42, 85)

    The geo distance between the two points is returned in kilometers
    """
    from math import radians, cos, sin, asin, sqrt

    lng_a = radians(float(pt_a[0]))
    lat_a = radians(float(pt_a[1]))

    lng_b = radians(float(pt_b[0]))
    lat_b = radians(float(pt_b[1]))
    # haversine formula
    dlng = lng_b - lng_a
    dlat = lat_b - lat_a
    whatevs = sin(dlat /2 ) ** 2 + cos(lat_a) * cos(lat_b) * sin(dlng / 2) ** 2
    c = 2 * asin(sqrt(whatevs))
    r = 6371 # Radius of earth in kilometers.
    # return the final calculation
    return c * r
