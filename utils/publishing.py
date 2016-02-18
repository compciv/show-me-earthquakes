from utils.filtrating import filtrate
from utils.geocoding import geocode
from utils.mapping import google_static_map_url, google_map_marker
from utils.settings import USGS_QUAKE_EVENT_BASEURL
import os.path

# HTML text templates
HTML_TEMPLATE_DIR = 'templates'
HTML_HEAD_FILENAME = os.path.join(HTML_TEMPLATE_DIR, 'head.html')
HTML_ROW_FILENAME  = os.path.join(HTML_TEMPLATE_DIR, 'row.html')
HTML_NARRATIVE_FILENAME  = os.path.join(HTML_TEMPLATE_DIR, 'narrative.html')
HTML_TAIL_FILENAME  = os.path.join(HTML_TEMPLATE_DIR, 'tail.html')

def publish(location):
    """
    What it expects:
    ----------------
    `location` is a string, representing some kind of human-readable
      geographical location

    `published_path` is a string representing a URL or filepath that
      the webbrowser can open.

    What it does:
    -------------
    Geocodes the location string.
    Then uses filtrate() to get the most relevant earthquakes
    Then produces HTML data that displays that data
    What it returns:
    ----------------
    A giant HTML string that can be written to file and opened as a webpage.
    """
    georesult = geocode(location)
    quakes = filtrate(georesult['longitude'], georesult['latitude'])

    #### let's make a big string of HTML
    giant_html_string = ""

    ##### Make the top of the page
    gmarkers = []
    for xid, quake in enumerate(quakes):
        latlng = str(quake['latitude']) + ',' + str(quake['longitude'])
        marker = google_map_marker(latlng, color="red", label=str(xid))
        gmarkers.append(marker)

    bigmap_url = google_static_map_url(markers = gmarkers, size="800x400")
    giant_html_string += html_head(quake_count=len(quakes),
                                   location=georesult['label'],
                                   map_url=bigmap_url)

    ##### Now add each quake as a "row"
    for q in quakes:
        latlngstr = "%s,%s" % (q['latitude'], q['longitude'])

        # each row has a bit of narrative text, which
        # I've put into its own function
        narrative_html = html_narrative(time=q['time'],
                                        place=q['place'],
                                        magnitude=q['mag'])

        # For each quake/row, just throw it onto the giant_html_string
        giant_html_string += html_row(
                        map_url=google_static_map_url(latlngstr, zoom = 12),
                        narrative=narrative_html,
                        quake_id=q['id'])
    ##### Now slap on the tail of the HTML
    giant_html_string += html_tail()

    ##### ...and we're done
    return giant_html_string


def friendly_timestamp(uglytimestamp):
    """
    uglytimestamp is something like:
        "2016-01-19T19:04:42.830Z"

    Returns:
        'Tuesday, January 16, 2016, 7:04 PM'
    """
    from dateutil import parser
    dateobj = parser.parse(uglytimestamp)
    return dateobj.strftime("%A, %B %y, %Y, %-l:%M %p")


def html_head(quake_count, location, map_url):
     with open(HTML_HEAD_FILENAME, 'r') as f:
        txt = f.read()
        return txt.format(quake_count=quake_count, location=location, map_url=map_url)

def html_row(narrative, map_url, quake_id):
     with open(HTML_ROW_FILENAME, 'r') as f:
        txt = f.read()
        quake_url = USGS_QUAKE_EVENT_BASEURL + quake_id

        return txt.format(narrative=narrative,
                          more_info_url=quake_url,
                          map_url=map_url)

def html_narrative(time, magnitude, place):
     with open(HTML_NARRATIVE_FILENAME, 'r') as f:
        txt = f.read()
        return txt.format(time=time, magnitude=magnitude, place=place)

def html_tail():
     with open(HTML_TAIL_FILENAME, 'r') as f:
        return f.read()
