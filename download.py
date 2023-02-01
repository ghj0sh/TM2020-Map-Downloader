import requests
import json
import wget
import os.path
import os

def loadConfig():
    cf = open("config.json", "r")
    cjson = json.loads(cf.read())
    author = cjson["TrackInformation"]["Author"]
    name = cjson["TrackInformation"]["Name"]
    tags = cjson["TrackInformation"]["Tags"]
    directorypath = cjson["DirectoryPath"]
    if directorypath == "":
        print("Error: You don't set the directory path on the file named config.json !")
        os._exit(0)
    verifyDirectory(directorypath, name, author, tags)
	
def verifyDirectory(directorypath, name, author, tags):
    if os.path.exists(directorypath):
        startDownload(directorypath, name, author, tags)
    else:
        print("Error: The directory path is not exist !")
		
def startDownload(directorypath, name, author, tags):
    print("Search for all maps with your settings on config.json");
    link = "https://trackmania.exchange/mapsearch2/search?api=on&limit=100"
    if tags == "":
        if name == "":
            if author == "":
                print("Chief, you cant just enter nothing.  Put something in here next time")
                time.sleep(3)
                os.exit(0)
            else:
                link = link+"&author="+author
        else:
            link = link+"&trackname="+name
            if author != "":
                link = link+"&author="+author
    else:
        link = link+"&tags="+tags
        if name != "":
            link = link+"&trackname="+name
            if author != "":
                link = link+"&author="+author
        else:
            if author != "":
                link = link+"&author="+author
    jsonres = json.loads(requests.get(link).text);
    print("Find: "+str(len(jsonres["results"]))+" maps on ManiaExchange !");
    print("Let's download !");
    for i in range(len(jsonres["results"])):
        trackid = jsonres["results"][i]["TrackID"];
        wget.download("https://trackmania.exchange/maps/download"+str(trackid), directorypath+str(jsonres["results"][i]["Name"])+".Map.Gbx");
        print("Downloading "+str((i+1))+"/"+str(len(jsonres["results"])))
		
		
def start():
    if os.path.isfile('config.json'):
        print("Load config...")
        loadConfig()
    else:
        print("Oh, I see, the configuration file isn't created !")
        print("I will created this");
        configcontains = {"TrackInformation" : {"Author" : "","Name" : "", "Tags" : ""},"DirectoryPath" : ""}
        f = open("config.json","w+")
        f.write(json.dumps(configcontains));
        os._exit(0)
		
start()
