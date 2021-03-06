from utils.filtrating import filtrate, haversine
from utils.settings import USGS_QUAKE_EVENT_BASEURL

def report(lng, lat):
    """

    Prints to screen interesting information about the 5 earthquakes nearest
     to a given geocoordinate point

    What it expects:
    ----------------
    lng (number) - a longitude coordinate
    lat (number) - a latitude coordinate

    What it does:
    -------------
    Calls filtrate(lng, lat) to get 5 closest records (as a list of dictionaries)

    Then it prints some kind of human-readable output. Note that this is
    different from filtrate() itself, which does not print anything
    but instead returns a list of dictionaries

    What it returns:
    ----------------
    Nothing. This is just for printing to screen for human readability
     as a warmup to producing
     the same kind of data in more attractive HTML format.
    """
    user_pt = (lng, lat)
    quakes = filtrate(lng, lat)

    for q in quakes:
        quake_pt = (float(q['longitude']), float(q['latitude']))
        distance = round(haversine(user_pt, quake_pt), 1)
        quake_url =  USGS_QUAKE_EVENT_BASEURL + q['id']
        infotxt = NARRATIVE_INFO_TEMPLATE.format(date=q['time'],
                                                 place=q['place'],
                                                 magnitude=q['mag'],
                                                 distance=distance,
                                                 quake_url=quake_url)
        print(infotxt)






NARRATIVE_INFO_TEMPLATE = """
On {date}, roughly {distance} km from you,
   a magnitude {magnitude} earthquake struck {place}.
   {quake_url}
"""
