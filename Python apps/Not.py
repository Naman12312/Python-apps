import urllib.request
import json
f = open("video.txt","w")
response = urllib.request.urlopen("https://youtu.be/OulN7vTDq1I")
f.write(response.read())