from utils.filtrating import filtrate, haversine
from utils.publishing import google_static_map_url, friendly_timestamp




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
        datestring = friendly_timestamp(q['time'])
        quake_pt = (float(q['longitude']), float(q['latitude']))
        distance = round(haversine(user_pt, quake_pt), 1)
        gmap_url = google_static_map_url((q['latitude'] + ',' + q['longitude']))

        infotxt = NARRATIVE_INFO_TEMPLATE.format(date=datestring,
                                       place=q['place'],
                                       magnitude=q['mag'],
                                       distance=distance,
                                       map_url=gmap_url)
        print(infotxt)






NARRATIVE_INFO_TEMPLATE = """
On {date}, roughly {distance} km from you,
   a M{magnitude} earthquake struck {place}.
   {map_url}
"""
