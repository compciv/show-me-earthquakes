# Sample Show-Me Project for Earthquakes

## How to get started

## How to download it

The [project homepage is here](https://github.com/compciv/show-me-earthquakes).

### Downloading via point-and-click

Uh, since this program runs from the command-line anyway, you'll _eventually_ want to open up your system shell. But if you're having `git` problems, you can download a ZIP file of the project the old-fashioned way via this URL:

[https://github.com/compciv/show-me-earthquakes/archive/master.zip](https://github.com/compciv/show-me-earthquakes/archive/master.zip)


### Downloading via the command-line

First, `cd` into a directory that you want to dump it to, e.g. `cd ~/Desktop` or `cd /tmp`.

Then download it using the `git clone` command -- it will automatically create a subdirectory named `show-me-earthquakes`:

~~~sh
git clone https://github.com/compciv/show-me-earthquakes
~~~

__Alternatively__, if you're having problems with `git`, you can download the URL via __curl__:

~~~sh
curl -Lo show-me-earthquakes.zip \
  https://github.com/compciv/show-me-earthquakes/archive/master.zip 
~~~

Then unzip that zip:

~~~sh
unzip show-me-earthquakes.zip
# this creates a subdirectory named show-me-earthquakes-master
# just rename it so the following instructions are consistent:
mv show-me-earthquakes-master/ show-me-earthquakes
~~~

Either way, via `git` or `curl` + `zip`, you should have a subdirectory named `show-me-earthquakes`. 

Change into the subdirectory:

~~~sh
cd show-me-earthquakes
~~~

Finally, you can run the program as you would any other Python script:

~~~sh
python woz.py
~~~







~~~
git clone 
cd show-me-earthquakes
python woz.py
~~~

### Directory structure

~~~
├── README.md
├── creds_mapzen.txt
├── data
│   ├── original
│   │   └── earthquakes.csv
│   └── wrangled-data.csv
├── utils
│   ├── __init__.py
│   ├── bootstrapping.py
│   ├── filtrating.py
│   ├── geocoding.py
│   ├── publishing.py
│   ├── reporting.py
│   ├── settings.py
│   └── wrangling.py
└── woz.py
~~~
