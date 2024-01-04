import speech_recognition as sr
import wavio
import sounddevice as sd
import time
fps = 44100
time.sleep(3)
duration = 10
recording = sd.rec(duration*fps, samplerate = fps, channels = 2)
sd.wait()
wavio.write("out.wav", recording, fps, sampwidth=2)

import pygame
pygame.init()
pygame.mixer.init()

op = pygame.mixer.music.load("out.wav")
pygame.mixer.music.play()
while True:
    pass