from ytPlaylist import ytPlaylist
from ytDownload import ytDownload
from spotifyUpload import spotifyUpload

channelURL = "https://www.youtube.com/playlist?list=PLZ1GiYqZoiH7QyULF8B7Wm5jeveptXaQG"
srcPath = "../spotify"
backupPath = "../backup"

if __name__ == "__main__":
    playlist = ytPlaylist(channelURL).newVideos
    fileNames = ytDownload(srcPath,playlist).fileNames
    spotifyUpload(fileNames)