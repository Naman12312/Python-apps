from gtts import gTTS

a = gTTS("Hello World")
a.save("a.mp3")

from playsound import playsound

playsound("a.mp3")