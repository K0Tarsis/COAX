import requests
from moviepy.editor import VideoFileClip
import os


link = "https://v16-webapp.tiktok.com/b6135b375383040ef6c1045b41bcffcc/62e8723f/video/tos/useast2a/tos-useast2a-ve-0068c004/68ba42ffc5674ce6803cd729c00a39e3/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=3402&bt=1701&btag=80000&cs=0&ds=3&ft=gKSYZ8hNo0PD1Wh44sg9wSX2O5LiaQ2D~AT&mime_type=video_mp4&qs=0&rc=NDw5MzpoaTg1NjNlODc6NkBpM2h0ZWY6ZndsZDMzNzczM0BjMTFgXzBfXzExLl4vX2EvYSNpazVgcjRfMG1gLS1kMTZzcw%3D%3D&l=202208011838380102171351372454704E"


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
    download(input())
    convert()
    print(os.path.abspath("TikTok.gif"))
