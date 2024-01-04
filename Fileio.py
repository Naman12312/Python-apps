# import pyttsx3
# from pyttsx3.drivers import *
# engine=pyttsx3.init()
# voices=engine.getProperty('voices')
# engine.setProperty('voice',voices[0].id)
# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()
f=open("naman.txt",'rt')
# cotent=f.read()
# for item in f:
#     print(item,end="\n")

print(f.readlines())
f.close()
# speak(cotent)