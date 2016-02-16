from utils.filtrating import filtrate
from utils.geocoding import geocode



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

    # let's make a big string
    html_text = ""
    # add the topper
    html_text += HTML_BOILERPLATE_HEAD.format(quake_count=len(quakes),
                                              location=georesult['label'])

    # for each quake, add HTML for the row
    for q in quakes:
        latlngstr = "%s,%s" % (q['latitude'], q['longitude'])
        narrative_html = HTML_NARRATIVE_TEXT.format(
            time=q['time'],
            place=q['place'],
            magnitude=q['mag']
        )

        html_text += HTML_BOILERPLATE_ROW.format(
            map_url=google_static_map_url(latlngstr),
            quake_id=q['id'],
            narrative=narrative_html
        )
    ## Now write the tail

    html_text += HTML_BOILERPLATE_TAIL
    # and we're done
    return html_text




# super lazy!
def google_static_map_url(marker):
    """
    marker is a string, e.g. "Ohio" or "34,-78.9"
    """
    basicurl = 'https://maps.googleapis.com/maps/api/staticmap?size=600x400&zoom=7'
    return basicurl + "&markers=" + marker


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



HTML_BOILERPLATE_HEAD = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>My Cool Webpage</title>
      <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css">
    </head>
    <body>
    <section class="container">
      <h1>Earthquakes near you!<h1>

      <p>
       Here are the <strong>{quake_count}</strong>
         closest earthquakes to {location}
        in the past <strong>30 days</strong>,
       according
       to the United States Geological Survey
       <a href="http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php>Earthquake Hazards Program.</a>
      </p>
"""

HTML_BOILERPLATE_ROW = """
<div class="row">
  <div class="col-sm-4">
    <img src="{map_url}" alt="map stuff">
  </div>
  <div class="col-sm-8">
      {narrative}
      <a href="http://earthquake.usgs.gov/earthquakes/eventpage/{quake_id}">
        Read more...
     </a>
  </div>
</div>
"""


HTML_NARRATIVE_TEXT = """
        <p>
         At <strong>{time}</strong>
         an earthquake of magnitude <strong>{magnitude}</strong>
         hit near <strong>{place}</strong>
        </p>
"""



HTML_BOILERPLATE_TAIL = """
    <p>Todo: Make a multi-marker Google Map to show all earthquakes at once.</p>

    <p>That is all. I am awesome!</p>
    <img src="http://placecage.com/800/500" alt="cage">

    </section>
</body>
</html>
"""
