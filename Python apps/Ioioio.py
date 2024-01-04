with open("me.txt","a") as f:
    rr=f.write('''
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman
I am Naman''')
print(rr)
with open("me.txt","rt") as f:
    rr=f.read()
print(rr)
f.close()
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str)
speak("H")