import json
from pytube import Playlist

class ytPlaylist():
    def __init__(self,channel):
        oldList = self.jsonRead()
        self.extractList(channel,oldList)

    def jsonRead(self):
        with open("./json/playlist.json", "r") as f:
            return json.load(f)

    def jsonWrite(self,data):
        with open("./json/playlist.json", "w") as f:
            json.dump(data,f)
    
    def extractList(self,channel,oldList):
        playlist = Playlist(channel)
        self.jsonWrite(list(playlist))
        self.newVideos = [x for x in playlist if x not in set(oldList)]
