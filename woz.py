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

if __name__ == '__main__':
    print("Available commands:")
    print(["bootstrap", "wrangle", "filtrate", "report", "publish"])
    the_command = input("What do you want to do? ")

    if the_command == 'hello':
        print("What is your name? ")
        username = input()
        print("Well, hello there, ", username.upper() + '!!!')

    elif the_command == 'help':
        print("Here is the documentation of the commands!")

        print("bootstrap")
        print(bootstrap.__doc__)

        print("wrangle")
        print(wrangle.__doc__)

        print("geocode")
        print(geocode.__doc__)

        print("filtrate")
        print(filtrate.__doc__)

        print("report")
        print(report.__doc__)

        print("publish")
        print(publish.__doc__)


    elif the_command == 'bootstrap':
        print("Let's bootstrap the data!")
        bootstrap()

    elif the_command == 'wrangle':
        print("Let's wrangle the data!")
        wrangle()

    elif the_command == 'geocode':
        print("Type in a location/address to geocode: ")
        user_location = input()
        georesult = geocode(user_location)
        # normally we pass the georesult dict into
        # another function that might use it
        # but since the user is using our simple text interface
        # we can just serialize it as text and
        # print it to screen
        print(json.dumps(georesult, indent=4))

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
        user_location = input("What is your current location/address? ")
        georesult = geocode(user_location)
        # if there is a valid, 'status' is "OK"; else it is None
        if georesult['status']:
            lng = georesult['longitude']
            lat = georesult['latitude']
            report(lng, lat)
        else:
            print("Your location", location, "did not return any results.")


    elif the_command == 'publish':
        user_location = input("What is your current location/address? ")
        html_txt = publish(user_location)
        print("Writing to:", LOCAL_WEBPAGE_PATH)
        sleep(2) # pausing...
        with open(LOCAL_WEBPAGE_PATH, 'w') as f:
            f.write(html_txt)

        print("Sending you to:", LOCAL_WEBPAGE_PATH)
        webbrowser.open(LOCAL_WEBPAGE_PATH)

    else:
        print("Did not recognize command", the_command)
