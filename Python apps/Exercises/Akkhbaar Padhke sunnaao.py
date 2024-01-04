import requests
import json
from win32com.client import Dispatch

def speak(str):
    print(str)
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)
data = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=ee17e6af8f6143f2af8758e2d2483dad").text
# print(data.text)
data = json.loads(data)
news = data['articles']
speak("Today's good news...")
for n1,n in enumerate(news):
    # print(n['title'])
    speak(n['title'])
    if n1==15:
        speak("News ended... thanks for listening...")
        break
    elif n1<15:    
        speak("Moving on to the next news.")
