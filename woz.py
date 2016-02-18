from utils import settings
from utils.settings import LOCAL_WEBPAGE_PATH
from utils.bootstrapping import bootstrap
from utils.wrangling import wrangle
from utils.geocoding import geocode
from utils.filtrating import filtrate
from utils.reporting import report
from utils.publishing import publish
from time import sleep
import webbrowser
import json
MY_COMMANDS = ["hello", "help", "bootstrap", "wrangle", "geocode",
               "filtrate", "report", "publish"]

def bolden(x):
    return '\033[1m' + str(x) + '\033[0m'

def bprint(*args):
    print(bolden(" ".join(args)))



if __name__ == '__main__':
    bprint("Welcome to Dan's program!")
    bprint("Available commands:")
    for cmdstr in MY_COMMANDS:
        print("\t- " + cmdstr)
    print()


    the_command = input(bolden("What do you want to do? "))

    if the_command == 'hello':
        username = input(bolden("What is your name? "))
        bprint("Well, hello there,", username.upper() + '!!!')

    elif the_command == 'help':
        bprint("Here is the documentation of the commands!")

        bprint("bootstrap")
        print(bootstrap.__doc__)
        bprint("wrangle")
        print(wrangle.__doc__)
        bprint("geocode")
        print(geocode.__doc__)
        bprint("filtrate")
        print(filtrate.__doc__)
        bprint("report")
        print(report.__doc__)
        bprint("publish")
        print(publish.__doc__)


    elif the_command == 'bootstrap':
        bprint("Let's bootstrap the data!")
        bootstrap()

    elif the_command == 'wrangle':
        bprint("Let's wrangle the data!")
        wrangle()

    elif the_command == 'geocode':
        user_location = input(bolden("Type in a location/address to geocode: "))
        georesult = geocode(user_location)
        # normally we pass the georesult dict into
        # another function that might use it
        # but since the user is using our simple text interface
        # we can just serialize it as text and
        # print it to screen
        serialized_results = json.dumps(georesult, indent=4)
        print(serialized_results)

    elif the_command == 'filtrate':
        # because input() ALWAYS takes what it is given and turns it
        # into text, we have to typecast it to float before sending it
        # to filtrate()
        print("Enter longitude: ")
        lng = float(input())
        print("Enter latitude: ")
        lat = float(input())

        results = filtrate(lng, lat)
        # turn it into proper text
        serialized_results = json.dumps(results, indent=2)
        # print to screen...nothing else to do
        print(serialized_results)

    elif the_command == 'report':
        user_location = input(bolden("What is your current location/address? "))
        georesult = geocode(user_location)
        # if there is a valid, 'status' is "OK"; else it is None
        if georesult['status']:
            lng = georesult['longitude']
            lat = georesult['latitude']
            report(lng, lat)
        else:
            bprint("Your location", location, "did not return any results.")


    elif the_command == 'publish':
        user_location = input(bolden("What is your current location/address? "))
        html_txt = publish(user_location)
        bprint("Writing to:", LOCAL_WEBPAGE_PATH)
        sleep(1) # pausing...
        with open(LOCAL_WEBPAGE_PATH, 'w') as f:
            f.write(html_txt)

        bprint("Sending you to:", LOCAL_WEBPAGE_PATH)
        webbrowser.open('file://' + LOCAL_WEBPAGE_PATH)

    else:
        bprint("Did not recognize command", the_command)

