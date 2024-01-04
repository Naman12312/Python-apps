import requests
import json
from win32com.client import Dispatch
# from setuptools import setup
# b = setup()
# import Pythonshell
def speak(str):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)
# speak("Hello, World!")
def getdata(url):
    r = requests.get(url=url)
    return r.text
# r = getdata("https://newsapi.org/")
# print(r)
r = requests.post("http://newsapi.org/v2/everything?q=tesla&from=2021-01-16&sortBy=publishedAt&apiKey=API_KEY")
r = json.loads(r.text)
print(r['message'])
# for i in range(0, 11):
speak(r['message'])