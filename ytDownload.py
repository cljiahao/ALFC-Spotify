import os
import re
import json
from yt_dlp import YoutubeDL
from datetime import datetime

class ytDownload():
    def __init__(self,srcPath,playlist):
        self.process(srcPath,playlist)
        print("done")
        self.renameFiles(srcPath)

    def process(self,srcPath,playlist):

        ydl_opts = {
            'format': 'mp3/bestaudio/best',
            'outtmpl': '{}/%(title)s.%(ext)s'.format(srcPath),
            'postprocessors': [{  # Extract audio using ffmpeg
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }]
        }

        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(playlist)

    def jsonRead(self):
        with open("./json/podcast.json", "r") as f:
            return json.load(f)

    def jsonWrite(self,data):
        with open("./json/podcast.json", "w") as f:
            json.dump(data,f)

    def renameFiles(self,srcPath):
        newPod, arr, self.fileNames = [],[],[]

        oldPod = self.jsonRead()

        for fileName in os.listdir(srcPath):
            match = re.search(r'\d{1,2} \b\w{1,4} \d{4}',fileName)
            for fmt in ('%d %b %Y','%d %B %Y'):
                try: 
                    newPod.append([datetime.strptime(match.group(), fmt).date(),fileName,False])
                    break
                except ValueError: pass
        
        
        if not self.jsonRead()[0][0]:
            sortDict = sorted(newPod) 
        else:
            oldPod = [[datetime.strptime(x[0], '%d %b %Y').date(),x[1],x[2]] for x in oldPod]
            sortDict = sorted(newPod+oldPod)

        for i, data in enumerate(sortDict):
            newName = f"{i+1}. ALFC Devotional - {datetime.strftime(data[0],'%d %b %Y')}.mp3"
            if not data[2]:
                self.fileNames.append(newName)
                os.rename(os.path.join(srcPath,data[1]),os.path.join(srcPath,newName))
            arr.append([datetime.strftime(data[0],'%d %b %Y'),newName,True])
        
        self.jsonWrite(arr)

            