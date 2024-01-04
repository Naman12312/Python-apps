from gtts import gTTS
import pygame
pygame.init()
pygame.mixer.init()
def speak(audio):
    t = gTTS(audio)
    t.save(audio + ".mp3")
    pygame.mixer.music.load(f"F:\\Downloads\\Python apps\\{audio}.mp3")
    pygame.mixer.music.play()
    pygame.time.delay(6000)
speak("Hello I am google assistant")