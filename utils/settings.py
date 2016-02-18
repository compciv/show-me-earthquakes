from os.path import join

# directories
DATA_DIR = 'tempdata'
ORIGINAL_DATA_DIR = join(DATA_DIR, 'original')

# various data files
ORIGINAL_DATA_FILENAME = join(ORIGINAL_DATA_DIR, 'earthquakes.csv')
WRANGLED_DATA_FILENAME = join(DATA_DIR, 'wrangled-data.csv')




# other useful files
GEOCODER_CREDENTIALS_FILENAME = 'creds_mapzen.txt'

# A place to throw a webpage on the local hard drive
LOCAL_WEBPAGE_PATH = join("/tmp", "myfunwebpage.html")


USGS_QUAKE_EVENT_BASEURL = "http://earthquake.usgs.gov/earthquakes/eventpage/"
