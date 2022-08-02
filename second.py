import requests
from moviepy.editor import VideoFileClip
import os


def download(link:str):
    r = requests.get(link, stream = True)

    with open('TikTok.mp4', 'wb') as f:
      for chunk in r.iter_content(chunk_size = 512*512):
        if chunk:
          f.write(chunk)


def convert():
    videoClip = VideoFileClip("TikTok.mp4")
    videoClip.write_gif("TikTok.gif")


if __name__ == "__main__":
    link = input()
    download(link)
    convert()
    print(os.path.abspath("TikTok.gif"))
