# download any Video from youtube
from pytube import YouTube
link = input('Enter Youtube Video Url :')
video = YouTube(link)
stream = video.streams.get_highest_resolution()
print("Downloading:", stream.title)
stream.download()
print('Download Done')
