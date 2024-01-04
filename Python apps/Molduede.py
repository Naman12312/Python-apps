import random
from win32com.client import *
x=['naman','harry sir','tripti','dhruv bhaiya']
x1=10
rand=random.choice(x)
# rand=1
def speak(str):
    s = Dispatch(("SAPI.SpVoice"))
    s.speak(str)
speak(rand)