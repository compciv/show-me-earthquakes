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


def google_static_map_url(markers, size="300x300", zoom="", center=""):
    """
    markers can either be a string,
        e.g. "Ohio" or "34,-78.9" (lat,lng) or "label:X|color:green|New York"
        or a collection of such strings
    """
    map_params = {"size": size, "zoom": zoom, "center": center, "markers": markers}
    query_string = urlencode(map_params, doseq=True)
    return GOOGLEMAP_ENDPOINT_URL + '?' + query_string
