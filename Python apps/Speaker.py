#import speech_recogniztion
while True:
    from win32com.client import *
    x=str(input())
    def speak(str):
        s=Dispatch(("SAPI.SpVoice"))
        s.speak(x)
    speak(x)
