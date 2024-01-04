'''
This is jarvis made by The GoldarmGang,

no one can edit this code except GoldarmGang who is me.
'''
# Import "chatbot" from
# chatterbot package.
from chatterbot import ChatBot # pip install chatterbot==1.0.4
import pyjokes
# Inorder to train our bot, we have
# to import a trainer package
# "ChatterBotCorpusTrainer"
from chatterbot.trainers import ChatterBotCorpusTrainer # pip install chatterbot_corpus


#then go to "C:\Users\User\AppData\Roaming\Python\Python38\site-packages\sqlalchemy\util\compat.py" or "C:\Users\User\AppData\Local\Python\Python38\site-packages\sqlalchemy\util\compat.py" and change the following line from:
"""
if win32 or jython:
    time_func = time.clock
else:
    time_func = time.time
"""
# to:
"""
if win32 or jython:
    try: # Python 3.4+
        preferred_clock = time.perf_counter
    except AttributeError: # Earlier than Python 3.
        preferred_clock = time.clock
else:
    time_func = time.time
"""
# Give a name to the chatbot Diana
# and assign a trainer component.
chatbot=ChatBot('Diana')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)
  
# Now let us train our bot with multiple corpus 
trainer.train()



import wikipedia #pip install wikipedia
import threading
import functools
from threading import Thread
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechrecognition, pip install pyaudio or if theres error then pip install pipwin then pipwin install pyaudio
import os
import webbrowser as wb
import datetime as dt
# from pyttsx3.drivers import sapi5 # pip install pyttsx3
import random
import smtplib
from playsound import playsound
from gtts import gTTS
import imaplib
import urllib.request
from bs4 import BeautifulSoup # pip install bs4
from youtube_search import YoutubeSearch # pip install Youtube-Search
# from win32ctypes import *# pip install pypiwin32
import threading
from tkinter import *
from PIL import Image, ImageTk # pip install pillow
from googlesearch import search # pip install googlesearch-python
import re
import requests
import json
import pickle

# from PyDictionary import PyDictionary
import time
os.chdir("D:\\drive D\\Downloads\\Python apps\\Jarvis")
root = Tk()
holoimg1 = Image.open("C:\\Users\\pinki\\Downloads\\holo.png")

holo = ImageTk.PhotoImage(holoimg1)
a = Label(image = holo)
a.pack()
x = 1


root.title("TheGoldarmGang")
root.wm_iconbitmap("j.ico")
root.geometry("644x567")
img = Image.open("a.png")

photo = ImageTk.PhotoImage(img)
resl = StringVar(root)
user = StringVar(root)
lvar = StringVar(root)
resl.set("")
resul = Label(root, font="lucida 10 bold", textvar=resl, wraplengt=644, bg="white")
resul.pack()
userl = Label(root,  font="lucida 14 bold", wraplengt=644, bg="white")
userl.pack(pady=34)
user.set("")
wres = StringVar(root)
wl = Label(root,  font="lucida 10 bold", wraplengt=644, bg="white")
wl.place(x = 0, y = 350)
ll = Label(root, font="lucida 14 bold", wraplengt=644, bg = "white")
ll.place(x = 170, y = 200)
root.configure(bg="black")
query_78 = StringVar()
# message_op = Entry(root, textvariable=query_78)
# message_op.pack()

def receive():
    a2 = open('D:\\drive D\\Downloads\\Python apps\\Jarvis\\TTS\\iposopsurhdhhdh74.pkl', 'rb')
    id67 = pickle.load(a2)
    a3 = open('D:\\drive D\\Downloads\\Python apps\\Jarvis\\TTS\\iposops.pkl', 'rb')
    iff = pickle.load(a3)
    print(type(id67))
    print(type(iff))
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login(id67,iff)
        mail.list()
        mail.select("inbox")
        result,data = mail.search(None,"ALL")
        idss = data[0]
        ids_list = idss.split()
        latest_email_id = ids_list[-1]
        result,data = mail.fetch(latest_email_id,"(RFC822)")
        raw_mail  = data[0][1]
        ma = re.compile("from")
        mae = ma.finditer(str(raw_mail))
        for mah in mae:
            print(mah)
        speak2(raw_mail)
        mail.close()
    except Exception as e:
        print(e)
        speak("Sorry. Sir error delected!")
    a2.close()
    a3.close()
voicename = 0
claaaas={'English':'https://us04web.zoom.us/j/5539880620?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09',
'Math':"https://us04web.zoom.us/j/5566339731?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09",
'Gk':'https://us04web.zoom.us/j/5539880620?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09',
'Hindi':'https://us04web.zoom.us/j/5419446487?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09',
'Sst':'https://us04web.zoom.us/j/5419446487?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09',
'Science':'https://us04web.zoom.us/j/4995676395?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09',
'Sanskrit':'https://us04web.zoom.us/j/4410645586?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09'}
x=random.randrange(1,21)
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(audio):
    global resl
    resl.set(f"Computer: {audio}")
    # engine.say(audio)

    # playsound('audio.mp3')
    root.update()
    
    # threading.Event().wait()
    # engine.stop()
    root.update()
    x = 1
    def say123():
        engine.say(audio)
        engine.runAndWait()
#Hello World This is Diana made by The GoldarmGang.
        root.update()
    
    say123()
    
    resl.set("Say Diana to speak...")
def speak2(audio):
    global wres
    wres.set(f"\n{audio}\n")
    engine.say(audio)
    
    root.update()
    engine.runAndWait()
    root.update()
    wres.set("")
def wishme():
    root.update()
    hour=int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning.")
    elif hour>=12 and hour<17:
        speak("good afternoon.")
    else:
        speak("good evening.")
    speak("How may I help you?")
    root.update()
ids={"naman":"namanthetoxic123@gmail.com","dhruv":"dhruv98110sharma@gmail.com","arush":"gameloop2021@gmail.com", "vinod":"vinodhodal@gmail.com", "subhash":"subhashhodal@gmail.com"}
def takecom():
    global resl
    global user
    root.update()
    r=sr.Recognizer()
    with sr.Microphone() as source:
        root.update()
        resl.set("listening....")  
        root.update()
        # print("listening....")
        # resl.set("listening....")
        r.pause_threshold=1
        audio=r.listen(source)
        root.update()
    try:
        root.update()
        # print("recognizing.....")
        resl.set("recognizing.....")
        query=r.recognize_google(audio)
        root.update()
        # print(f"user: {query}\n")
        user.set(f"User: {query}\n")
        root.update()

        resl.set("Say Diana to speak...")
        root.update()

        # user.set("")
        
    except Exception as e:
        # print(e)
        speak("Sorry, I can't hear you. say that again.")
        return "None"
        root.update()
    # resl.set("recognizing.....")
    return query
# with open("TTS\\don't open its nessesary.txt",'r') as f:
#     iff=f.read()
# print(iff)

def fullScreen(event):
    root.attributes('-fullscreen',True) 
def notFullScreen(event):
    root.attributes('-fullscreen',False)
root.bind("<KeyPress-F11>", fullScreen)
root.bind("<KeyPress-F10>", notFullScreen)
def sendemail(to,sub,content):
    a = open('D:\\drive D\\Downloads\\Python apps\\Jarvis\\TTS\\iposopsurhdhhdh74.pkl', 'rb')
    id1234 = pickle.load(a)
    a45 = open('D:\\drive D\\Downloads\\Python apps\\Jarvis\\TTS\\iposops.pkl', 'rb')
    iff = pickle.load(a45)
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(id1234,iff)
    server.sendmail(id1234,to,f"Subject: {sub}\n\n{content}")
    server.close()
    a.close()
def takecom2():
    print('o')
    # root.protocol('WM_DELETE_WINDOW', root.withdraw) 
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # resl.set("listening....")  

        # print("listening....")
        # resl.set("listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        # print("recognizing.....")
        # resl.set("recognizing.....")
        query=r.recognize_google(audio,language='en-in')

        # print(f"user: {query}\n")
        # user.set(f"User: {query}\n")

        # resl.set("Press mic to listen...")


        # user.set("")
    
    except Exception as e:
        # print(e)
        # speak("Sorry, I can't hear you. say that again.")
        return "None"
    return query

if __name__ == "__main__":
        wishme()
        def opopop():
            resl.set("Say Diana to speak...")
            op = takecom2().lower()
            print(op.lower())
            aopui = open("2name.txt")
            if 'deewana' in op.lower() or 'diana' in op.lower() or "deeana" in op.lower() or "divana" in op.lower():
                # print(op)
                
                
                
                print('h')
                main()
            
            if aopui.read() in op.lower():
                print("h")
                main()
        
            else:
                opopop()
            aopui.close()
        def main():
            speak("Yes?")
            query=takecom().lower()

            if 'wikipedia' in query:
                opi = search(query,tld='co.in', num_results=1)
                wb.get().open_new_tab(opi[0])
            elif "+" in query:
                try:
                    query=query.replace("=","")
                    t = eval(query)
                    speak(f"{query} = {t}")
                except Exception as e:
                    print(e)
                    speak("What? I think there is something wrong.")
            elif "-" in query:
                try:
                    query=query.replace("=","")
                    t = eval(query)
                    speak(f"{query} = {t}")
                except Exception as e:
                    print(e)
                    speak("What? I think there is something wrong.")
            #only for linux
            elif 'volume' in query:
                query  = query.replace("volume", '')
                query = query.replace("%", '')
                os.system(f"sudo amixer -q -D pulse sset Master {query}%")
            elif 'mute' in query:
                query  = query.replace("volume", '')
                query = query.replace("%", '')
                os.system(f"sudo amixer -q -D pulse sset Master toggle")
            
            elif 'unmute' in query:
                query  = query.replace("volume", '')
                query = query.replace("%", '')
                os.system(f"sudo amixer -q -D pulse sset Master 100%")
            elif "stop" in query:
                os.system("killall firefox")
            elif "pause" in query:
                import pyautogui
                pyautogui.press("space")
            
            elif "resume" in query:
                import pyautogui
                pyautogui.press("space")
            elif "change your name" in query:
                speak("Sorry. you can't change my name...")
                speak("But you can call me something else...")
                speak("What do you want to call me???")
                uiyui = takecom()
                speak("Are you sure?")
                opopp = takecom().lower()
                if opopp=="yes" or "y":
                    speak(f"Ok, you can call me {uiyui} from now.")
                    with open("2name.txt", 'w') as f:
                        f.write(uiyui)
                else:
                    speak("Ok.")
            elif "microsoft edge" in query:
                speak("Opening... Microsoft edge")
                os.startfile("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")
            elif "who are you" in query:
                speak("I am Diana and i want love")
            elif "name" in query:
                speak("My name is Diana.")
            elif "how are you" in query:
                speak("I am totally fine. just tell how may i help you?")
                # wb.get().open(search(f"{query}")[0])
            elif "mad" in query:
                speak("mad. and me. never.")
            elif "meaning" in query:
                wb.get().open(f"https://www.google.com/search?q={query}&oq={query}&aqs=chrome..69i57j35i39l2j69i60l5.2631j0j9&sourceid=chrome&ie=UTF-8")
            elif "bluestacks" in query:
                speak("Opening... bluestacks...")
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\BlueStacks 5")
            elif "blue stacks" in query:
                speak("Opening... bluestacks...")
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\BlueStacks 5")
            elif "news" in query:
                data = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=ee17e6af8f6143f2af8758e2d2483dad").text
                # print(data.text)
                data = json.loads(data)
                news = data['articles']
                speak("News for today...")
                for n1,n in enumerate(news):
                    # print(n['title'])
                    if n1==20:
                        break
                    speak(n['title'])
                    if n1<20:    
                        speak("Moving on to the next news.")
                speak("News Ended. Thanks for listening...")
                speak("For more, go to https://www.hindustantimes.com/india-news")
            elif "sing a song" in query:
                speak("Here is a song for you...")
                l = ["""
    Before we eat, we wash, wash our hands, Before we eat we wash, wash our hands, We play, play, play, then we wash the germs away, Before we eat, we wash, wash, wash our hands.
            ""","""
    Twinkle, twinkle, little star, How I wonder what you are!, Up above the world so high, Like a diamond in the sky. When the blazing sun is gone,When he nothing shines upon,Then you show your little light,Twinkle, twinkle, all the night.
                ""","""
    oh ohh ohh. my personall, my personal ohhmy personal assistant,we can work at the office late,take long lunch breaks. wont you be? my personal assistant, i dont mind givin you a raise, all your vacations are paid, wont you be?,
    """
    """


    """]
                i = random.choice(l)
                speak(i)
                wres.set("")
            elif "song" in query:
                query=query.replace("play","")
                query=query.replace("youtube","")
                # query=query.replace("song","")
                try:
                    speak(f"Playing {query} on youtube")
                    from youtube_search import YoutubeSearch
                    results = YoutubeSearch(f"{query}", max_results=1).to_dict()
                    res = results[0]['url_suffix']
                    wb.get().open(f"https://youtube.com{res}")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. Error delected.")
            elif "play" in query:
                query=query.replace("play","")
                query=query.replace("youtube","")
                query=query.replace("song","")
                query=query.replace("open", "")
                try:
                    speak(f"Playing... {query} on youtube")
                    from youtube_search import YoutubeSearch
                    results = YoutubeSearch(f"{query}", max_results=1).to_dict()
                    res = results[0]['url_suffix']
                    wb.get().open(f"https://youtube.com{res}")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. Error delected.")
            elif "video" in query:
                query=query.replace("play","")
                query=query.replace("youtube","")
                query=query.replace("song","")
                query=query.replace("open", "")
                try:
                    speak(f"Opening... {query} on youtube")
                    from youtube_search import YoutubeSearch
                    results = YoutubeSearch(f"{query}", max_results=1).to_dict()
                    res = results[0]['url_suffix']
                    wb.get().open(f"https://youtube.com{res}")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. Error delected.")

            elif "open google" in query:
                wb.get().open_new_tab('https://google.com')
            elif 'please open the google' in query:
                wb.get().open_new_tab('https://google.com')
            elif "open youtube" in query:
                wb.get().open_new_tab('https://youtube.com')
            elif "open stack overflow" in query:
                wb.get().open_new_tab('https://stackoverflow.com')
            elif "open whatsapp" in query:
                wb.get().open_new_tab('https://web.whatsapp.com')
            elif "open codewithharry" in query:
                wb.get().open_new_tab('https://codewithharry.com')
            elif "open roms forever" in query:
                wb.get().open_new_tab('https://romsforever.com')
            elif "open filehippo" in query:
                wb.get().open_new_tab('https://filehippo.com')
            elif "open drive" in query:
                wb.get().open_new_tab('https://drive.google.com')
            elif "open meet" in query:
                wb.get().open_new_tab('https://meet.google.com')
            elif "open translate" in query:
                wb.get().open_new_tab('https://translate.google.com')
            elif "open play emulator" in query:
                wb.get().open_new_tab('https://playemulator.com')
            elif "open obs" in query:
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OBS Studio\\OBS Studio (64bit)")
            # elif "play music" in query:
            #     music_dir="F:\\home pc\\my pandrive data\\songs"
            #     songs=os.listdir(music_dir)
            #     print(songs)
            #     os.startfile(os.path.join(music_dir,songs[8]))
            elif "any song" in query:
                songs = ['closer','on and on','three machine racing queen','attention'] 
                rsongs = random.choices(songs)
                try:
                    speak("Playing some music on youtube.")
                    from youtube_search import YoutubeSearch
                    results = YoutubeSearch(f"{rsongs}", max_results=1).to_dict()
                    res = results[0]['url_suffix']
                    wb.get().open(f"https://youtube.com{res}")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. Error delected.")


            elif "the time" in query:
                time=dt.datetime.now().strftime("%H:%M:%S")
                print(time)
                speak(f"the time is:{time}")
            elif "open zoom" in query:
                zooom="C:\\Users\\Naman Sharma\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
                os.startfile(zooom)
            elif "class" in query:
                print("Which class you want to attend???")
                speak("Which class you want to attend???")
                claaas=takecom()
                wb.get().open(f"{claaaas[claaas]}")
            elif "open chrome" in query:
                chrome="C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"
                os.startfile(chrome)
            elif "open brave" in query:
                brave="C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
                os.startfile(brave)
            elif "open code" in query:
                query=query.replace("visual","")
                query=query.replace("studio","")
                query=query.replace("vs","")
                os.system("code")
                
            elif "open visual studio code" in query:
                
                os.system("code")
            elif "open vs code" in query:
                #vs_code="C:\\Users\\Naman Sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                # os.startfile(vs_code)
                os.system("code")
            elif "open word" in query:
                word="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word"
                os.startfile(word)
            elif "open power point" in query:
                power="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Powerpoint"
                os.startfile(power)
            elif "open excel" in query:
                excel="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel"
                os.startfile(excel)
            elif "open one note" in query:
                one="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OneNote 2016"
                os.startfile(one)
            elif "open access" in query:
                access="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Access"
                os.startfile(access)
            elif "open publisher" in query:
                publisher="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Publisher"
                os.startfile(publisher)
            elif "open skype" in query:
                os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Skype for Business")
            elif "open notepad" in query:
                speak("Opening... Notepad")
                notepad="F:\\Downloads\\Python apps\\dist\\Notepad++.exe"
                os.startfile(notepad)
            elif "open word pad" in query:
                wordpad="C:\\Windows\\write.exe"
                os.startfile(wordpad)
            elif "calculator" in query:
                c="F:\\Downloads\\Python apps\\Dist\\OOPS Calculator\\OOPS Calculator.exe"
                os.startfile(c)
            elif "open obs studio" in query:
                obs="C:\\Program Files\\obs-studio\\bin\\64bit\\obs64.exe"
                os.startfile(obs)
            elif "super mario maker" in query:
                smm="C:\\Users\\Naman Sharma\\Desktop\\Citra_VS2017_Qt5.9.1_generic_sandbox_20171107\\citra-qt.exe"
                os.startfile(smm)
            elif "open super mario 3d land" in query:
                sm3dl="C:\\Users\\Naman Sharma\\Desktop\\canary-mingw\\citra-qt.exe"
                os.startfile(sm3dl)
            elif "snake" in query:
                snake="F:\\Downloads\\Python apps\\snake.py"
                os.startfile(snake)
            elif "quit" in query:
                speak("Quitting sir. Thanks for the time.")
                exit()
            elif "internet explorer" in query:
                wb.open_new_tab("msn.com")
            elif "open rapid typing" in query:
                rapid="C:\\Program Files (x86)\\RapidTyping 5\\RapidTyping.exe"
                os.startfile(rapid)
            elif "open teams" in query:
                a = "C:\\Users\\Naman Sharma\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams"
                teams="C:\\Users\\Naman Sharma\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Teams"
                os.startfile(teams)
            elif "open pycharm" in query:
                pycharm="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.2\\bin\\pycharm64.exe"
                os.startfile(pycharm)
            elif "open duo" in query:
                wb.get().open("https://duo.google.com")
            elif "open maps" in query:
                wb.get().open("https://maps.google.com")
            elif "open softonic" in query:
                wb.get().open("https://www.softonic.com")
            elif "open programiz" in query:
                wb.get().open("https://www.progrmiz.com")
            elif "open udemy" in query:
                wb.get().open("https://www.udemy.com")
            elif "open python.org" in query:
                wb.get().open("https://docs.python.org")
            elif "open paint" in query:
                paint="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Paint"
                os.startfile(paint)
            elif "open snipping tool" in query:
                snipping="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Snipping Tool"
                os.startfile(snipping)
            elif "google" in query:
                # query=query.replace("google","")
                speak("This is what I found on Google...")
                # wb.get().open(search(f"{query}")[0])
                wb.get().open(f"https://www.google.com/search?q={query}&oq={query}&aqs=chrome..69i57j35i39l2j69i60l5.2631j0j9&sourceid=chrome&ie=UTF-8")

            elif "song" in query:
                query=query.replace("play","")
                query=query.replace("youtube","")
                # query=query.replace("song","")
                try:
                    speak(f"Playing {query} on youtube")
                    from youtube_search import YoutubeSearch
                    results = YoutubeSearch(f"{query}", max_results=1).to_dict()
                    res = results[0]['url_suffix']
                    wb.get().open(f"https://youtube.com{res}")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. Error delected.")
            elif "music" in query:
                query=query.replace("play","")
                query=query.replace("youtube","")
                query=query.replace("music","")
                try:
                    speak(f"Playing {query} music on youtube")
                    from youtube_search import YoutubeSearch
                    results = YoutubeSearch(f"{query}", max_results=1).to_dict()
                    res = results[0]['url_suffix']
                    wb.get().open(f"https://youtube.com{res}")
                except Exception as e:
                    print(e)
                    speak("Sorry sir. Error delected.")
            elif "date" in query:
                d=dt.date.today()
                print(d)
                speak(f"today's date is:{d}")
            elif "play catch" in query:
                p="F:\\Downloads\\Python apps\\catch.py"
                os.startfile(p)     
            elif "open python apps" in query:
                python="D:\\drive D\\Downloads\\Python apps"
                os.startfile(python)
            elif "watch movies" in query:
                speak("Opening Netflix")
                wb.get().open_new_tab("netflix.com")
            elif "bing" in query:
                query=query.replace("bing","")
                speak("According to bing...")
                wb.get().open(f"https://www.bing.com/search?q={query}&form=QBLH&sp=-1&pq=&sc=0-0&qs=n&sk=&cvid=DE9D8F29B3A54984BDF7D3BA3CF327B2")
            elif "stack overflow" in query:
                query=query.replace("stack overflow","")
                speak("According to stackoverflow...")
                wb.get().open(f"https://stackoverflow.com/questions/tagged/{query}")
            elif "program is " in query:
                query=query.replace("programmiz","")
                speak("According to programmiz")
                wb.get().open(f"https://www.programiz.com/search/{query}")
            
            elif "open tekken 6" in query:
                tekken="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PPSSPP"
                os.startfile(tekken)
            elif "hub" in query:
                wb.get().open("https://github.com")
            elif "geeks for geeks" in query:
                wb.get().open("https://www.geeksforgeeks.com")
            elif "geeksforgeeks" in query:
                wb.get().open("https://www.geeksforgeeks.org")
            # elif "hub" in query:
            #     wb.get().open("https://github.com/new")
            elif "who created you" in query:
                speak("The GoldArmGang aka Naman Sharma created me.")
            elif "who made you" in query:
                speak("The GoldArmGang aka Naman Sharma created me.")
            elif "why are you created" in query:
                speak("Thanks to The GoldArmGang, beyond is a secret.")
            elif "why are you made" in query:
                speak("Thanks to The GoldArmGang, beyond is a secret.")
            elif "i love you" in query:
                speak("It's harder to understand....")
            elif "open slides" in query:
                wb.get().open("https://docs.google.com/presentation/u/0/")
            elif "open docs" in query:
                wb.get().open("https://docs.google.com/document/u/0/")
            elif "open sheets" in query:
                wb.get().open("https://docs.google.com/spreadsheets/u/0/")
            elif "open books" in query:
                wb.get().open("https://books.google.co.in/bkshp?hl=en&tab=rp")
            elif "open classroom" in query:
                wb.get().open("https://classroom.google.com/h")
            elif "open news" in query:
                wb.get().open("https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en")
            elif "weather" in query:
                import requests, json
 
# Enter your API key here
                api_key = "418fdb38c7d5134fca63dc6304cf2efc"
                
                # base_url variable to store url
                base_url = "http://api.openweathermap.org/data/2.5/weather?"
                
                # Give city name
                city_name = "delhi"
                
                # complete_url variable to store
                # complete url address
                complete_url = base_url + "appid=" + api_key + "&q=" + city_name
                
                # get method of requests module
                # return response object
                response = requests.get(complete_url)
                
                # json method of response object
                # convert json format data into
                # python format data
                x = response.json()
                
                # Now x contains list of nested dictionaries
                # Check the value of "cod" key is equal to
                # "404", means city is found otherwise,
                # city is not found
                if x["cod"] != "404":
                
                    # store the value of "main"
                    # key in variable y
                    y = x["main"]
                
                    # store the value corresponding
                    # to the "temp" key of y
                    current_temperature = y["temp"]
                
                    # store the value corresponding
                    # to the "pressure" key of y
                    current_pressure = y["pressure"]
                
                    # store the value corresponding
                    # to the "humidity" key of y
                    current_humidity = y["humidity"]
                
                    # store the value of "weather"
                    # key in variable z
                    z = x["weather"]
                
                    # store the value corresponding
                    # to the "description" key at
                    # the 0th index of z
                    weather_description = z[0]["description"]
                
                    # print following values
                    speak(" Temperature  = " +
                                    str(int(current_temperature-273.15)) + "°C" +
                        "\n atmospheric pressure (in hPa unit) = " +
                                    str(current_pressure) +
                        "\n humidity (in percentage) = " +
                                    str(current_humidity) +
                        "\n description = " +
                                    str(weather_description))
                
                else:
                    print(" City Not Found ")
            elif "send email to" in query:
                try:
                    query = query.replace("send email to ","")
                    speak("What is your subject???")
                    o = takecom()
                    speak("What should i say?")
                    Content=takecom()
                    speak("Sending your email...")
                    sendemail(ids[query],o,Content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("I have to appologize for this.")
                    speak("Sorry Sir. i am not able to send this email")
            elif "send email" in query:
                try:
                    query = query.replace("send email","")
                    speak("Whom to send? These are your gmail contacts:")
                    lvar.set("""
                    Naman,
                    Dhruv,
                    Arush,
                    Vinod,
                    Subhash
                    """)
                    man = takecom()
                    speak("What is your subject???")
                    o = takecom()
                    speak("What should i say?")
                    Content=takecom()
                    speak("Sending your email...")
                    sendemail(ids[man.lower()],o,Content)
                    lvar.set("")
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("I have to appologize for this.")
                    speak("Sorry Sir. i am not able to send this email")
            elif "brainly" in query:
                speak("According to brainly...")
                query=query.replace("brainly","")
                wb.get().open(f"https://brainly.in/app/ask?q={query}")
            elif "codewithharry" in query:
                speak("ok...")
                query=query.replace("codewithharry","")
                wb.get().open(f"https://codewithharry.com/videos/{query}")
            elif "ppsspp" in query:
                speak("Opening ppsspp")
                ppsspp="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PPSSPP"
                os.startfile(ppsspp)
            # elif "rpcs3" in query:
            #     speak("opening rpcs3")
            #     rpcs3="F:\\Downloads\\rpcs3-v0.0.14-11579-3567c43f_win64\\rpcs3.exe"
                # os.startfile(rpcs3)
            elif "onedrive" in query:
                speak("opening. onedrive")
                onedrive="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\SkyDrive Pro 2013"
                os.startfile(onedrive)
            elif "python" in query:
                speak("opening. python")
                python123="C:\\Python3\\python.exe"
                os.startfile(python123)
            elif "onenote" in query:
                onenote="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\OneNote 2013"
                speak("opening. onenote")
                os.startfile(onenote)
            elif "infopath designer" in query:
                visio="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\InfoPath Designer 2013"
                speak("opening. infopath")
                os.startfile(visio)
            elif "infopath filler" in query:
                visio="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\InfoPath Filler 2013"
                speak("opening. infopath")
                os.startfile(visio)
            elif "send to onenote" in query:
                speak(f"Opening... {query}")
                a = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Send to OneNote 2013"
            elif "gmail" in query:
                wb.get().open("https://mail.google.com")
            elif "skype" in query:
                speak("opening. skype.")
                skype="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Lync 2013"
                os.startfile(skype)
            # elif "project" in query:
            #     print("opening. project") 
            #     speak("opening. project")
            #     project="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\"
            #     os.startfile(project)
            elif "outlook" in query:
                speak("opening. outlook")
                outlook="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Outlook 2013"
                os.startfile(outlook)
            elif "friend" in query:
                query=query.replace("friend","")
                speak(f"{query} don't want to be your friend.")
                speak("want to retry???")
                retry=takecom()
                if retry=="yes":
                    speak("sorry nothing will happen if you retry.")
                elif retry=="no":
                    speak("very good.")
            elif "remind me when" in query:
                a = query
                query = query.replace("remind")
                query = query.replace("me")
                query = query.replace("when")
                query = query.replace("there")
                query = query.replace("is")
                query = query.replace("minutes")
                query = query.replace("hours")
                query = query.replace("ours")
                query = query.replace("seconds")
                import time
                if "hours" in a:

                    time.sleep({query*3600})
                elif "ours" in a:

                    time.sleep({query*3600})
                elif "minutes" in a:

                    time.sleep({query*60})
                elif "seconds" in a:

                    time.sleep({query})
                
            elif "sticky notes" in query:
                sticky="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Sticky Notes"
                speak("opening. sticky notes")
                os.startfile(sticky)    
            elif "say" in query:
                query=query.replace("say","")
                speak(f"{query}")
            # elif "remind" in query:
            #     try:
            #         hour1 = int(dt.datetime.now().hour)
            #         # print(hour1)
            #         print("What you want to set in reminder???")
            #         speak("What you want to set in reminder???")
            #         remind = takecom()
            #         speak(f"{remind} At what time????")
            #         timee=takecom()
            #         speak("Reminder set!!!") 
            #         timti = int(timee)
            #         # print(timti)
            #         if timti>=hour1:
            #             print(f"Time to {remind}!")
            #             speak(f"Time to {remind}")
            #             speak(f"Time to {remind}")
            #             speak(f"Time to {remind}")
            #             speak(f"Time to {remind}")
            #             speak(f"Time to {remind}")
            #             speak(f"Time to {remind}")
            #             speak(f"Time to {remind}")
            #     except Exception as e:
            #         print(e)
            #         print("Sorry Naman error delected!")         
            #         speak("Sorry Naman. error delected!")      
            elif "voice" in query:
                engine.setProperty('voice',voices[1].id)
                speak("voice changed!")
            

            elif "receive email" in query:
                speak("Searching for a new email...")
                receive()

            elif "none" in query:
                pass
            elif "yahoo" in query:
                query=query.replace("yahoo","")
                speak("According to yahoo...")
                wb.get().open(f"https://in.search.yahoo.com/search?p={query}&fr=yfp-t&fr=yfp-t-s&fp=1&toggle=1&cop=mss&ei=UTF-8")
            elif "ask" in query:
                query=query.replace("ask","")
                speak("according to ask...")
                wb.get().open(f"https://www.ask.com/web?o=0&l=dir&qo=homepageSearchBox&q={query}")    
            # elif "dragon" in query:
            #     speak("Opening... Electro Dragon's Battle...")
            #     idr = "F:\\Downloads\\Dragon Game\\dist\\Main\\Main.exe"
            #     os.startfile(idr)
            elif "bye" in query:
                speak("Quitting sir. Thanks for the time.")
                # root.destroy()
                exit()
            elif "exit" in query:
                speak("Exitting sir... Thanks for the time.")
                exit()
            elif "clock" in query:
                speak("Opening... Clock")
                os.startfile("F:\\Downloads\\Python apps\\Dist\\Clock\\Clock.exe")
            elif "site" in query:
                query=query.replace("site","")
                query=query.replace("open","")
                query=query.replace("webpage","")
                speak("Opening... webpage")
                # print(search(f"{query}"))
                wb.get().open(search(f"{query}")[0])
            elif "i am bad" in query:
                speak("You are a good person.")
            elif "what can you do" in query:
                speak("I can do anything. try saying something...")
            elif "i am happy" in query:
                speak("If you are happy then I am happy.")
            # elif "i am sad" in query:
            #     speak("You can play Electro Dragon's Battle...")
            #     idr = "F:\\Downloads\\Dragon Game\\dist\\Main\\Main.exe"
            #     os.startfile(idr)
            elif "calculate" in query:
             
                app_id = "XGVP59-K9VGUQ46W6"
                client = wolframalpha.Client(app_id)
                indx = query.lower().split().index('calculate')
                query = query.split()[indx + 1:]
                res = client.query(' '.join(query))
                answer = next(res.results).text
                print("The answer is " + answer)
                speak("The answer is " + answer)
            elif "joke" in query:
                speak(pyjokes.get_joke)
                # speak(a)
                # time.sleep(1)
                
                # speak(b)
                # query = takecom().lower()
            elif "screenshot" in query:
                from PIL import ImageGrab
                imgage = ImageGrab.grab()
                speak("What's the name of your image?")
                name = takecom()
                if not os.path.exists(name):

                    imgage.save(name+".jpg")
                    imgage.show()
                else:
                    speak(f"There is already a file named {name}.jpg in this directory.")
            elif "pixlr" in query:
                speak("Opening... Pixlr")
                wb.get().open("https://pixlr.com/e/")
            elif "inpixio" in query:
                speak("Opening... Inpixio...")
                wb.get().open("https://www.inpixio.com/")
            elif "inpixio remove" in query:
                speak("Opening... Inpixio Remove Background...")
                wb.get().open("https://www.inpixio.com/remove-background/")
            elif "hello" in query:
                speak("Yes... say Diana to speak...")
            elif "remind" in query:
                speak("Tell me the task you want to do later.")
                task = takecom()
                speak(f"At what time you want to do {task}?")
                speak("Type the time in the terminal.")
                timetk = input("Time: ")
                speak(f"Ok, you will get notified when its {timetk}")
                speak("And keep these two windows open.")
                task23 = open("Task23.txt", "w")
                task23.write(task)
                Time_ = open("TTime.txt", "w")
                Time_.write(timetk)
                os.startfile("remind.py")
            # elif "cortana":
            #     speak("She is the virtual assistant made by microsoft.")
            #     speak("Say cortana to call her.")
            elif "reminder" in query:
                speak("Tell me the task you want to do later.")
                task = takecom()
                speak(f"At what time you want to do {task}?")
                timetk = takecom()
                speak(f"Ok, you will get notified when its {timetk}")
                speak("And keep these two windows open.")
                task23 = open("Task23.txt", "w")
                task23.write(task)
                Time_ = open("TIME23.txt", "w")
                Time_.write(timetk)
                os.startfile("remind.py")
            else:
                user.set(f'User:{query}')
                print(query)
                speak("Please Wait...")
                import wolframalpha
                try:
                    query = query.replace('hey diana' , '')
                    query = query.replace('hi diana' , '')
                    query = query.replace('diana' , '')
                    # query = query.replace('who is', '')
                    app_id = "XGVP59-K9VGUQ46W6"
                    client = wolframalpha.Client(app_id)
                    res = client.query(query)
                    answ = next(res.results).text
                    speak(answ)
                except Exception as e:
                    try:
                        print("Wikipedia")
                        import wikipedia
                        
                        query = query.replace("who is","")
                        query = query.replace("which is", "")
                        query = query.replace("what is", "")
                        # print(query)
                        resultop = wikipedia.summary(str(query), sentences=2, auto_suggest=False)
                        speak(resultop)
                    except Exception as e:
                        try:
                            print("Wikipedia")
                            import wikipedia
                            
                            query = query.replace("who is","")
                            query = query.replace("which is", "")
                            query = query.replace("what is", "")
                            # print(query)
                            resultop = wikipedia.summary(str(query), sentences=2, auto_suggest=True)
                            speak(resultop)
                        except Exception as e:
                            response = chatbot.get_response(query)
                            speak(response)
        # print(op)     
            # resl.set("")    
            root.after(100,opopop())

        opopop()  
        # main()
        

            # wb.get().open(search(f"{query}")[0])
        # root.update_idletasks()
root.update()    
# Button(root, image=photo, command=opopop().).place(x = 300, y = 340)

root.mainloop()
''' 
Code will update day by day...
Creator: The GoldarmGang
'''
# Helo Wrodl