# Sample Show-Me Project for Earthquakes

# How to get started

This is a sample project that's meant to demonstrate how your project will work. The details will differ, but the flow is the same.

So try to copy this project (via the instructions below) and run it. You can put it anywhere and then delete it after you're done. Also, make sure you have a Mapzen Search API key.


## How to download it

Use `git clone` from the system shell's command line.

This will create a new subdirectory named `show-me-earthquakes` wherever you run the command from. So you might want to move into a directory that you want to save it in (i.e. NOT YOUR OWN COMPCIV FOLDER):

~~~sh
$ cd ~/Desktop
~~~


Then download it using the `git clone` command -- it will automatically create a subdirectory named `show-me-earthquakes`:

~~~sh
$ git clone https://github.com/compciv/show-me-earthquakes
~~~

It should work even if you don't have a Github account.


If it works, you can change into that subdirectory like so:

~~~
$ cd show-me-earthquakes
~~~


### Downloading via point-and-click

Note: I don't recommend doing it this way. Use __git clone__ instead, as described in the next section...because since this program runs from the command-line anyway, you'll _eventually_ want to open up your system shell. But if you're having `git` problems, you can download a ZIP file of the project the old-fashioned way via this URL:

[https://github.com/compciv/show-me-earthquakes/archive/master.zip](https://github.com/compciv/show-me-earthquakes/archive/master.zip)

Double clicking that zip will make a new folder named:


Now you just have to get into that folder via the command-line...i.e. if you saved it into your `~/Downloads` folder, you can do this:

~~~sh
$ cd ~/Downloads/show-me-earthquakes-master
~~~



## Trying it out

When you're in the projects directory, uou can run the program as you would any other Python script:

~~~sh
python woz.py
~~~



Running `woz.py` should take you to a prompt like this:

![image welcome.png](sample-data/assets/welcome.png)

And you should be able to try out any of those commands. For now, try the `"hello"` command:

![img](sample-data/assets/hello-quakes.gif)


### Getting a geocoding error

If you run the `geocode` command, you'll get an error:

~~~
Exception: ('Expecting credentials file at:', 'creds_mapzen.txt')
~~~


## Add your Mapzen key

It means what it says. So create a new file in the current directory named `creds_mapzen.txt`, then paste in your actual Mapzen API key, e.g.

      search-xxyyzz

Then try the `geocode` command again. It should give you a response like this:

~~~
Type in a location/address to geocode: Stanford, CA
{
    "label": "Stanford, Santa Clara County, CA",
    "longitude": -122.16608,
    "latitude": 37.42411,
    "text": "Stanford, CA",
    "confidence": 0.6,
    "status": "OK",
    "country": "United States"
}
~~~


### Seeing a webpage

Ultimately, your project will respond to a __publish__ command that will behave similarly to this demo project. But see if it works for you in the demo project. First you have to run `python woz.py` and run the following two commands:

- `bootstrap`
- `wrangle`

Then run it again, but run the `publish` command:

![img](sample-data/assets/hello-nic-cage.gif)


# That's all...

At this point, just make sure you can copy this project, run it on your own computer, and get a feel of how I expect things to be.

For now. I'll update you when this Github repo updates with more specific information. - Dan










