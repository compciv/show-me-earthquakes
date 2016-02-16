from utils.settings import GEOCODER_CREDENTIALS_FILENAME
from copy import copy # used to make a copy of the params dict
                      # so we don't accidentally mutate it...
import requests
import os.path
API_ENDPOINT = 'https://search.mapzen.com/v1/search'
API_DEFAULT_PARAMS = {"size": 1}


def geocode(location_string):
    """
    Attempt to geocode a location string using Mapzen Search API

    What it expects:
    ----------------
    `location_string` is a string, representing some kind of human-readable
      geographical location

    What it does:
    -------------
    Calls the Mapzen Search API via a HTTP request, using the
    api key stored in CREDS_FILE

    What it returns:
    ----------------
    A dictionary containing these key-value pairs:

    - status: is "OK" if at least one result was returned, else: None
    - text: "the thing you searched for" (string) - basically, the location argument,
        which may be useful to ANOTHER function that deals with this dict result
    - gid: "something:99999" (string) - this comes with Mapzen data
    - layer: "layer name" (string) - another piece of metadata from Mapzen
    - country: "Canada" (string) - a useful way to filter out results that are waaaay off
    - confidence: 0.95 (float) - a number from 0 to 1 representing how confident Mapzen is about its search
    - latitude: 99.99 (number)
    - longitude: "-122.222" (number)

    If the geocoder returns no response with eligible results,
    a dictionary is still returned, except it has just two keys:

      - text: is still set to the location string that was searched for
      - status: is just None
    """
    result = {"text": location_string, "status": None}
    data = query_geocoding_service(location_string)
    if data['features']: # it has at least one feature...
        feature = data['features'][0] # pick out the first one
        props = feature['properties']  # just for easier reference
        coords = feature['geometry']['coordinates'] # easier reference

        # now populate that dictionary
        result['status'] = 'OK'
        result['country'] = props['country']
        result['confidence'] = props['confidence']
        result['label'] = props['label']
        result['longitude'] = coords[0]
        result['latitude'] = coords[1]
    # note that if the if branch isn't entered...i.e. Mapzen
    # couldn't find _any_ features
    # the `result` dictionary is still returned at the end of the program
    # But it is mostly empty and contains a "status" of None
    #  which the function caller can use in deciding to ignore
    #  the response
    return result

def query_geocoding_service(location_string):
    """
    given a location string, this queries the Mapzen Search API
    and returns its response as a dictionary (i.e not raw JSON)
    """
    my_params = copy(API_DEFAULT_PARAMS)
    my_params['api_key'] = get_creds()
    my_params['text'] = location_string
    resp = requests.get(API_ENDPOINT, params=my_params)
    return resp.json()

def get_creds():
    """
    open that credentials file, read its contents (strip the newline)
    and return the resulting string
    """
    if os.path.exists(GEOCODER_CREDENTIALS_FILENAME):
        return open(GEOCODER_CREDENTIALS_FILENAME).read().strip()
    else:
        raise Exception("Expecting credentials file at:", GEOCODER_CREDENTIALS_FILENAME)
