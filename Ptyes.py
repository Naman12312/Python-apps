import pyttsx3
engine=pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("helllo")
# second way
from win32com.client import Dispatch
def speak2(str):
    s = Dispatch(("SAPI.SpVoice"))
    s.Speak(str)
speak2("helllo")
