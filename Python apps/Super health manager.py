from win32com.client import *
def speak(str):
    s=Dispatch(("SAPI.SpVoice"))
    s.speak(str)
while 1:   
    import os
    import sys
    import time
    t1=time.time()
    print("welcome to the health manager i can help you to remain healthy type your name here\n")
    speak("welcome to the health manager i can help you to remain healthy type your name here")
    x=str(input())
    print("what do you want to lock options are:\ndiet,\nexercise")
    speak("what do you want to lock options are: diet,exercise")
    x1=str(input())
    if x1=="diet":
        print("when you ate food last time?")
        speak("when you ate food last time?")
        x2=str(input())
        print("eat food after 2or3 hours")
        speak("eat food after 2or3 hours")
        print("how many times you eat in each day?")
        speak("how many times you eat in each day?")
        x3=int(input())
        if x3>3:
            print("you must eat only 3 times a day otherwise you will get obese or fat")
            speak("you must eat only 3 times a day otherwise you will get obese or fat")
        elif x3<3:
            print("eat three times a day to remain healthy")
            speak("eat three times a day to remain healthy")
        elif x3==3:
            print("ok this is good you eat normal times a day")
            speak("ok this is good you eat normal times a day")
        print("are you suffring from some disease???")
        speak("are you suffring from some cummunicable disease???")
        x4=str(input())
        if x4=="yes":
            print("go to a hospital and take rest, get well soon")
            speak("go to a hospital and take rest, get well soon")
        if x4=="no":
            print("ok")
            speak("ok")
            print("you are healthy")
            speak("you are healthy")
        else:
            print("you need to follow my guides to remain healthy")
            speak("you need to follow my guides to remain healthy")
    elif x1=="exercise":
        print("do you go to walk everyday??")
        speak("do you go to walk everyday??")
        x5=str(input())
        if x5=="yes":
         print("ok good if you come home from walking eat food after 10 or 15 minutes")
         speak("ok good if you come home from walking eat food after 10 or 15 minutes")
        print("do you exercise regularly???")
        speak("do you exercise regularly???")
        x6=str(input())
        if x6=="no":
            print("you must do some yoga asans ,you can see some yoga asans on https://www.nytimes.com/guides/well/beginner-yoga")
            speak("you must do some yoga asans ,you can see some yoga asans on https://www.nytimes.com/guides/well/beginner-yoga")
        elif x6=="yes":
            print("good if you want more yoga aasans you can check them on https://www.nytimes.com/guides/well/beginner-yoga")
            speak("good if you want more yoga aasans you can check them on https://www.nytimes.com/guides/well/beginner-yoga")
        print("do you play everyday for 1 hr???")
        speak("do you play everyday for 1 hr???")
        x7=str(input())
        if x7=="no":
            print("you must play for 1 hr otherwise you will be weak")
            speak("you must play for 1 hr otherwise you will be weak")
        elif x7=="yes":
            print("good if you play your body gets more attractive")
            speak("good if you play your body gets more attractive")
        print("do you sleep early and wake up early???")
        speak("do you sleep early and wake up early???")
        x8=str(input())
        if x8=="yes":
            print("ok")
            speak("ok")
        if x8=="no":
            print("you must sleep early and get up early because a good sleep is a proper rest")
            speak("you must sleep early and get up early because a good sleep is a proper rest")
        print("are you suffring from some non-cummunicable disease???")
        speak("are you suffring from some non-cummunicable disease???")
        x9=str(input())
        if x9=="yes":
            print("eat food normal times and exercise regularly to get well soon")
            speak("eat food normal times and exercise regularly to get well soon")
            print("you are not healthy")
            speak("you are not healthy")
        else:
            print("you are healthy")
            speak("you are healthy")