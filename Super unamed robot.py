while True:
    from tkinter import *
    from tkinter.ttk import *
    import pyttsx3
    engine=pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")
    engine.setProperty("voice",voices[1].id)
    def speak(audio):
        engine.say(audio)
        engine.runAndWait()
    def h() :
                speak("tell me your name i can tell about you")
                name=str(input("tell me your name i can tell about you\n"))
                
                print ("hi", name)
                speak("hi")
                speak(name)
                if name==("GoldarmGang"):
                    print ("your hobby is playing VALORANT")
                    speak("your hobby is playing VALORANT")
                    print ("you made me")
                    speak("you made me")
                elif name==("tripti"):
                    print ("your hobby is learning japanese")
                    speak("your hobby is learning japanese")
                elif name==("vinod"):
                    print ("you are the chacha ji of my father you are my grandfather")
                    speak("you are the chacha ji of my father you are my grandfather")
                elif name==("punya"):
                    print ("you are the friend of my father")
                    speak("you are the friend of my father")
                elif name==("what is your name"):
                    speak("I don't have a name can you give me a name?")
                    c=str(input("I don't have a name can you give me a name?"))
                    print("my name is",c)
                    speak("my name is")
                    speak(c)
                    print ("you have gived me a very nice name")
                    speak("you have gived me a very nice name")
                    print ("thank you")
                    speak("thank you")
                elif name==("neelam"):
                    print ("you are chachi of my father naman")
                    speak("you are chachi of my father naman")
                    print ("you are a good teacher in hindi")
                    speak("you are a good teacher in hindi")
                elif name==("subhash"):
                    print ("you are the father of my father you are my grandfather")
                    speak("you are the father of my father you are my grandfather")
                    print("your hobby if repairing computers")
                    speak("your hobby if repairing computers")
                elif name==("pinki"):
                    print ("you are the mother of my father you are my grandmother")
                    speak("you are the mother of my father you are my grandmother")
                    print ("you are a teacher in adarsh school")
                    speak("you are a teacher in adarsh school")
                elif name==("ramnivaas"):
                    print ("you are the grandfather of my father you are my grand grandfather")
                    speak("you are the grandfather of my father you are my grand grandfather")
                    print ("your hobby is repairing watches")
                    speak("your hobby is repairing watches")
                elif name==("bhagvandevi"):
                    print ("you are  grandmother of my father")
                    speak("you are  grandmother of my father")
                    print("you are my grand grandmother")
                    speak("you are my grand grandmother")
                elif name==("vidushi"):
                    print ("your hobby is trying something new")
                    speak("your hobby is trying something new")
                elif name==("vaibhav"):
                    print ("you are also a friend of my father")
                    speak("you are also a friend of my father")
                elif name==("krishnam"):
                    print("you are also a friend of my father")
                    speak("you are also a friend of my father")
                elif name==('sumit'):
                    print ("you are the brother of my father")
                    speak("you are the brother of my father")
                    print ("your hobby is playing games")
                    speak("your hobby is playing games")
                elif name==("mayank"):
                    print("you are a friend of my father")
                    speak("you are a friend of my father")
                    print("your hobby is english writing")
                    speak("your hobby is english writing")
                else:
                    print ("I don't know you")
                    speak("I don't know you")
    h()
