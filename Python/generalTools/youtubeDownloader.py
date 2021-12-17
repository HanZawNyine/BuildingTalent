from pytube import Playlist
from pytube import Channel
from pytube import YouTube

class YoutubeDownloader:
    def __init__(self,url:str):
        self.url = url

    def playlistDownload(self):
        p = Playlist(self.url)
        for a in p.video_urls:
            #print("Play List Of urls : "+ a)
            self.url = a
            self.SingleVideoyoutubeDownload()

    def SingleVideoyoutubeDownload(self):
        myVideo = YouTube(self.url)
        fileSizeInBytes = myVideo.streams.filter(progressive="True").get_highest_resolution()
        print(myVideo.title)

        MaxFileSize = fileSizeInBytes.filesize / 1024000
        MB = str(MaxFileSize) + " MB"
        print("File Size : {:00.00f} MB".format(MaxFileSize))

        fileSizeInBytes.download()
        print(myVideo.title+"...Completed url : "+self.url)

    def ChannelAllDownload(self):
            # download Channel
            # url = 'https://www.youtube.com/channel/UCvVZ19DRSLIC2-RUOeWx8ug'
            c = Channel(self.url)
            print(f"Channel Of Video : {len(c.video_urls)}")
            for a in c.video_urls:
                self.url = a
                #print(f'url : {a}')
                self.playlistDownload()

if __name__ == '__main__':
    url = 'https://www.youtube.com/channel/UCM3v8UhSt61avksfEb7ttJA'
    youtube = YoutubeDownloader(url)
    # youtube.SingleVideoyoutubeDownload()
    # youtube.playlistDownload()
    #youtube.ChannelAllDownload()

#python -m pip install pytube