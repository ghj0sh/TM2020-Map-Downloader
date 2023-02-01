# TM2020-Map-Downloader
A python script that lets you download a list of Trackmania maps.

# How to download it ?

Download the source code in the top right (green box that says code)

Make sure you have python.  If you dont, download it and make sure to add it to your PATH

Dependencies:
wget
requests
json

If you dont know how to, go into cmd and type "pip install (whatever)" for all 3.
This shouldn't be an issue, though.

The EXE does NOT work with Trackmania-Exchange.  USE THE PYTHON SCRIPT!

# How to configure it

When you run the program once using "python download.py", it'll create a .json file in the folder that you're running it in.

I'm not sure what happened to the original person's code, but for some reason it wont add the necessary stuff to the .json

If it does that, copy and paste this into the .json file:

```
{
	"TrackInformation": {
		"Author": "",
		"Name": "",
		"Tags": ""
	},
	"DirectoryPath": ""
}
```

Im not sure if DirectoryPath works since it just downloads to my downloads folder anyways.  Might fix it later

# How to Change the TMX Exchange

Did you just figure out that TM2020 requires Standard Access to play the game?  Well, so did I, which is why Im here to tell you how to change the site so you download from a different exchange.

STEP 1: Choose a trackmania exchange and make a note of the link

STEP 2: Go to https://api2.mania.exchange and go to the corresponding exchange

STEP 3: Copy the API stuff for searching a track

STEP 4: Paste it into your link.  Should look something like this, for example: https://tmnf.exchange/api/tracks?limit=100

STEP 5: Paste the link into line 27 in replacement of https://trackmania.exchange/mapsearch2/search?api=on&limit=100

STEP 6: Look at how a map is downloaded on the exchange (look at how the map download link is formatted).

STEP 7: Paste that into line 54 in replacement of https://trackmania.exchange/maps/download (Example for TMNF: https://tmnf.exchange/trackgbx)

NOTE: You might have to change everything around for it to work properly with the exchange you want it to work with.  Sometimes its not a simple copy/paste type of deal.  Read over the API docs and how they work.
# CREDIT

Shineeeeeuh - Making the code (https://github.com/Shineeeeeuh/Trackmania-Map-Downloader)

Me - Editing it to make it work with Trackmania Exchange (not hard)

# TO-DO
- fix json file

- maybe just remove json alltogether

- make tutorial on how to make this work with other TMX sites
