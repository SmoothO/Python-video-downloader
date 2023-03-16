import os

# /*pip install pytube*\  run this command before running this code

from pytube import YouTube

def Download(link):
    youtube = YouTube(link)
    youtube = youtube.streams.get_highest_resolution()
    try:
        youtube.download()
    except:
        print("An error has occurred")
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)


