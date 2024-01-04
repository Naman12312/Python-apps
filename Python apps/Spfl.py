from win32com.client import Dispatch
def speak(str):
    s = Dispatch(("SAPI.SpVoice"))
    s.Speak(str)
speak("Hello world")