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
# CREDIT

Shineeeeeuh - Making the code (https://github.com/Shineeeeeuh/Trackmania-Map-Downloader)
Me - Editing it to make it work with Trackmania Exchange
