# for youtube library
import requests
from pprint import pprint
from pytube import YouTube
from bs4 import BeautifulSoup

def download_videoFrom_youtube(url, savePath):
    yt = YouTube(url)
    pprint(yt.get_videos())
    print(yt.filename)
    #yt.set_filename()
    video = yt.get('mp4', '360p')
    video.download(savePath)

# To Extract the video url from youtube page.
def extract_href(url, savePath):
   source_code = requests.get(url).text
   Soup = BeautifulSoup(source_code,"html.parser")
   for vurl in Soup.findAll('a', {'class': 'yt-uix-sessionlink yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 spf-link '}):
            href = vurl.get('href')
            print(str(href))
            hreff=href.split('=')
            print(hreff[1])
            download_videoFrom_youtube('https://youtu.be/'+hreff[1], savePath)



 # calling download videos
def start():
     print("Hi ! this is YTrending.")
     dtv = input("Press 1: Downloading trending videos: ")
     asv = input("Press 2 : To download any specific videos: ")
     if dtv == '1':
         savePath = input('share path to save videos: ')
         urlTy = "https://www.youtube.com/feed/trending"
         extract_href(urlTy, savePath)

start()