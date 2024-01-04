import speech_recognition as sr
import random
swg=['snake','water','gun']
er=random.choices(swg)
def com():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print("you:",query)
    except Exception as e:
        print("say that again please...")
        return "None"
    return query


while True:
    query=com().lower()
    print("i:",er)
    if "snake" in query and er==['gun']:
        print("you lose!!!")
    elif "gun" in query and er==['snake']:
        print("you win")
    elif "gun" in query and er==['water']:
        print("you lose!!!")
    elif "water" in query and er==['snake']:
        print("you lose!!!")
    elif "snake" in query and er==['water']:
        print("you win!!!")
    elif "water" in query and er==['gun']:
        print("you win!!!")
    else:
        print("tie!!")