from utils.settings import ORIGINAL_DATA_FILENAME, WRANGLED_DATA_FILENAME
import csv

def wrangle():
    """
    Remove earthquake records that we don't care about
    What it expects:
    ----------------
    ORIGINAL_DATA_FILENAME points to a CSV file that follows the
     standard USGS earthquakes record data format

    What it does:
    -------------
    There's not much wrangling to be done...but for the heck of it,
    we'll remove any record that doesn't have a 'status' of 'reviewed'
    and/or is not actually an 'earthquake' (the USGS tracks quarry explosions, too)

    This function:
    - opens ORIGINAL_DATA_FILENAME
    - parses it as a CSV into a list of dicts
    - filters out the records (dicts) that aren't 'reviewed' 'earthquakes'
    - saves the remaining records to WRANGLED_DATA_FILENAME

    What it returns:
    ----------------
    Nothing, though it does print out how many records are in the
     WRANGLED_DATA_FILENAME

    """
    with open(ORIGINAL_DATA_FILENAME, 'r') as infile:
        txtlines = infile.read().splitlines()
    records = list(csv.DictReader(txtlines))
    wrangled_records = []
    print(ORIGINAL_DATA_FILENAME, "has", len(records), 'records')
    for r in records:
        if r['status'] == 'reviewed' and r['type'] == 'earthquake':
            wrangled_records.append(r)


    # wrangled_records is a list of dicts
    # it needs to be serialized to text...using csv.DictWriter
    # is the easiest way to write the text to disk
    with open(WRANGLED_DATA_FILENAME, 'w') as outfile:
        # The DictWriter requires a fieldnames argument...
        # which is a list of column names. Grab the "keys"
        # from any dict in wrangled_records
        # let's just pop out the first dictionary and use its keys:
        columnheaders = wrangled_records[0].keys()
        # pass those into the fieldnames argument
        c = csv.DictWriter(outfile, fieldnames=columnheaders)
        # and write all the wrangled_records at once
        c.writeheader()
        c.writerows(wrangled_records)

    # let's just get a count of how many records were "wrangled" out
    print(WRANGLED_DATA_FILENAME, "has", len(wrangled_records), 'records')


