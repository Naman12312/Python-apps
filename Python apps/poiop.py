# import pyttsx3
# engine = pyttsx3.init('sapi5')
# engine.setProperty('languages', 'hi')
# engine.say('tum kaise ho?')
# engine.runAndWait()
from gtts import gTTS
a = gTTS("तुम कैसे हो?")
a.save('a.mp3')