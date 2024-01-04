'''
this is jarvis made by naman sharma
no one can edit this code except naman sharma who is me
'''
import wikipedia #pip install wikipedia
import pyttsx3 #pip install pyttsx3 or pip install pyttsx3==2.71 (if doesn't work.)
import speech_recognition as sr #pip install speechrecognition
import os
import webbrowser as wb
import datetime as dt
from pyttsx3.drivers import sapi5
import random
import smtplib
import imaplib
import urllib.request
from bs4 import BeautifulSoup
from youtube_search import YoutubeSearch # pip install Youtube-Search
# from win32ctypes import *# pip install pypiwin32
import threading
from tkinter import *
from PIL import Image, ImageTk # pip install pillow
from googlesearch import search # pip install googlesearch-python
import re
import requests
import json
root = Tk()
root.title("Jarvis")
root.wm_iconbitmap("F:\\downloads\\Python apps\\2.ico")
root.geometry("644x567")
img = Image.open("F:\\downloads\\2.ico")
photo = ImageTk.PhotoImage(img)
resl = StringVar(root)
user = StringVar(root)
resl.set("")
resul = Label(root, textvar=resl, font="lucida 19 bold", wraplengt=644, bg="light blue")
resul.pack(pady=34)
userl = Label(root, textvar=user, font="lucida 19 bold", wraplengt=644, bg="light blue")
userl.pack(pady=34)
user.set("")
wres = StringVar(root)
wl = Label(root, textvar=wres, font="lucida 10 bold", wraplengt=644, bg="light blue")
wl.place(x = 0, y = 300)
root.configure(bg="light blue")
def receive():
    try:
        mail = imaplib.IMAP4_SSL("imap.gmail.com")
        mail.login("subhashhodal808@gmail.com",iff)
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
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',193)
def speak(audio):
    global resl
    resl.set(f"Computer: {audio}")
    engine.say(audio)
    root.update()
    engine.runAndWait()
    # threading.Event().wait()
    # engine.stop()
    root.update()
    resl.set("Press mic to listen...")
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
        speak("good morning Sir.")
    elif hour>=12 and hour<17:
        speak("good afternoon Sir.")
    else:
        speak("good evening Sir.")
    speak("How may I help you?")
    root.update()
ids={"naman":"subhashhodal808@gmail.com","dhruv":"dhruv98110sharma@gmail.com","arush":"gameloop2021@gmail.com"}
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
        query=r.recognize_google(audio,language='en-in')
        root.update()
        # print(f"user: {query}\n")
        user.set(f"User: {query}\n")
        root.update()

        resl.set("Press mic to listen...")
        root.update()

        # user.set("")
        
    except Exception as e:
        # print(e)
        speak("say that again please....")
        return "None"
        root.update()
    # resl.set("recognizing.....")
    return query
with open("F:\\home pc\\my pandrive data\\ACROBAT-7.0\\don't open its nessesary.txt",'r') as f:
    iff=f.read()
def sendemail(to,sub,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('subhashhodal808@gmail.com',iff)
    server.sendmail('subhashhodal808@gmail.com',to,f"Subject: {sub}\n\nMessage: {content}")
    server.close()
if __name__ == "__main__":
    wishme() 
    def main():
        query=takecom().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia...., Please wait....")
            query=query.replace("wikipedia","")
            try:
                results=wikipedia.summary(query,sentences=3)
                speak("Alright!")
                speak("Wikipedia says...")
                # speak2(results)
                # speak2(results)
                # results = results.split("\n\n\n")
                # speak2(results[0:100])
                # speak2(results[100:200])
                # speak2(results[200:300])
                speak2(results)
                wres.set("")
            except Exception as e:
                print(e)
                speak("Sorry sir. error delected.")
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
        elif "*" in query:
            try:
                query=query.replace("=","")
                t = eval(query)
                speak(f"{query} = {t}")
            except Exception as e:
                print(e)
                speak("What? I think there is something wrong.")
        elif "multiply" in query:
            try:    
                query=query.replace("multiply","*")
                t = eval(query)
                speak(f"{query} = {t}")
            except Exception as e:
                print(e)
                speak("What? I think there is something wrong.")
        elif "divide" in query:
            try:
                query=query.replace("divide","/")
                t = eval(query)
                speak(f"{query} = {t}")
            except Exception as e:
                print(e)
                speak("What? I think there is something wrong.")
        elif "plus" in query:
            try:    
                query=query.replace("plus","+")
                t = eval(query)
                speak(f"{query} = {t}")
            except Exception as e:
                print(e)
                speak("What? I think there is something wrong.")
        elif "minus" in query:
            try:
                query=query.replace("minus","-")
                t = eval(query)
                speak(f"{query} = {t}")
            except Exception as e:
                print(e)
                speak("What? I think there is something wrong.")
        elif "/" in query:
            try:
                query=query.replace("=","")
                t = eval(query)
                speak(f"{query} = {t}")
            except Exception as e:
                print(e)
                speak("What? I think there is something wrong.")
        elif "who are you" in query:
            speak("I am Jarvis and i want love")
        elif "name" in query:
            speak("My name is Jarvis, Naam to sunaa hogaa")
        elif "how are you" in query:
            speak("I am totally fine. just tell how may i help you?")
        elif "who" in query:
            speak("This is what I found on Google...")
            wb.get().open(f"https://www.google.com/search?sxsrf=ALeKk002Ym5y6AR87ae1uuTTMcsBsMz3og%3A1610097643995&source=hp&ei=6yP4X7S8OsLmz7sP4oWdyAo&q={query}&oq={query}&gs_lcp=CgZwc3ktYWIQAzIHCC8MQyQMQJzIECCMQJzIECCMQJzIECAAQQzIHCAAQsQMQQzIECAAQQzIECAAQQzIKCC4QxwEQowIQQzIICAAQsQMQgwEyBAgAEENQ3Q5Y3Q5g4xRoAHAAeACAAYkBiAGJAZIBAzAuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwj03fyQgYzuAhVC83MBHeJCB6kQ4dUDCAc&uact=5")
        elif "mad" in query:
            speak("mad. and me. never.")
        elif "meaning" in query:
            query=query.replace("meaning","")
            query=query.replace("what","")
            query=query.replace("is","")
            query=query.replace("the","")
            query=query.replace("of","")
            query=query.replace("in","")
            query=query.replace("hindi","")
            query=query.replace("english","")
            query=query.replace(" ","")
            from PyDictionary import PyDictionary
            dictionary=PyDictionary()
            speak(dictionary.meaning(query))
        
        elif "what" in query:
            speak("This is what I found on Google...")
            wb.get().open(f"https://www.google.com/search?sxsrf=ALeKk002Ym5y6AR87ae1uuTTMcsBsMz3og%3A1610097643995&source=hp&ei=6yP4X7S8OsLmz7sP4oWdyAo&q={query}&oq={query}&gs_lcp=CgZwc3ktYWIQAzIHCC8MQyQMQJzIECCMQJzIECCMQJzIECAAQQzIHCAAQsQMQQzIECAAQQzIECAAQQzIKCC4QxwEQowIQQzIICAAQsQMQgwEyBAgAEENQ3Q5Y3Q5g4xRoAHAAeACAAYkBiAGJAZIBAzAuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwj03fyQgYzuAhVC83MBHeJCB6kQ4dUDCAc&uact=5")
        elif "why" in query:
            speak("This is what I found on Google...")
            wb.get().open(f"https://www.google.com/search?sxsrf=ALeKk002Ym5y6AR87ae1uuTTMcsBsMz3og%3A1610097643995&source=hp&ei=6yP4X7S8OsLmz7sP4oWdyAo&q={query}&oq={query}&gs_lcp=CgZwc3ktYWIQAzIHCC8MQyQMQJzIECCMQJzIECCMQJzIECAAQQzIHCAAQsQMQQzIECAAQQzIECAAQQzIKCC4QxwEQowIQQzIICAAQsQMQgwEyBAgAEENQ3Q5Y3Q5g4xRoAHAAeACAAYkBiAGJAZIBAzAuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwj03fyQgYzuAhVC83MBHeJCB6kQ4dUDCAc&uact=5")
        elif "how" in query:
            speak("This is what I found on Google...")
            wb.get().open(f"https://www.google.com/search?sxsrf=ALeKk002Ym5y6AR87ae1uuTTMcsBsMz3og%3A1610097643995&source=hp&ei=6yP4X7S8OsLmz7sP4oWdyAo&q={query}&oq={query}&gs_lcp=CgZwc3ktYWIQAzIHCC8MQyQMQJzIECCMQJzIECCMQJzIECAAQQzIHCAAQsQMQQzIECAAQQzIECAAQQzIKCC4QxwEQowIQQzIICAAQsQMQgwEyBAgAEENQ3Q5Y3Q5g4xRoAHAAeACAAYkBiAGJAZIBAzAuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwj03fyQgYzuAhVC83MBHeJCB6kQ4dUDCAc&uact=5")
        elif "open google" in query:
            wb.get().open_new_tab('https://google.com')
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
            vs_code="C:\\Users\\Naman Sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_code)
        elif "open visual studio code" in query:
            vs_code="C:\\Users\\Naman Sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_code)
        elif "open vs code" in query:
            vs_code="C:\\Users\\Naman Sharma\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_code)
        elif "open word" in query:
            word="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Word 2013"
            os.startfile(word)
        elif "open power point" in query:
            power="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\PowerPoint 2013"
            os.startfile(power)
        elif "open excel" in query:
            excel="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Excel 2013"
            os.startfile(excel)
        elif "open one note" in query:
            one="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\OneNote 2013"
            os.startfile(one)
        elif "open access" in query:
            access="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Access 2013"
            os.startfile(access)
        elif "open publisher" in query:
            publisher="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Publisher 2013"
            os.startfile(publisher)
        elif "open notepad" in query:
            speak("Opening... Notepad")
            notepad="F:\\Downloads\\Python apps\\dist\\Notepad++.exe"
            os.startfile(notepad)
        elif "open word pad" in query:
            wordpad="C:\\Windows\\write.exe"
            os.startfile(wordpad)
        elif "calculate" in query:
            c="F:\\Downloads\\Python apps\\dist\\simple calculator.exe"
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
            root.destroy()
        elif "internet explorer" in query:
            wb.open_new_tab("msn.com")
        elif "open rapid typing" in query:
            rapid="C:\\Program Files (x86)\\RapidTyping 5\\RapidTyping.exe"
            os.startfile(rapid)
        elif "open teams" in query:
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
            speak("These results are back from a search...")
            wb.get().open(f"https://www.google.com/search?sxsrf=ALeKk002Ym5y6AR87ae1uuTTMcsBsMz3og%3A1610097643995&source=hp&ei=6yP4X7S8OsLmz7sP4oWdyAo&q={query}&oq={query}&gs_lcp=CgZwc3ktYWIQAzIHCC8MQyQMQJzIECCMQJzIECCMQJzIECAAQQzIHCAAQsQMQQzIECAAQQzIECAAQQzIKCC4QxwEQowIQQzIICAAQsQMQgwEyBAgAEENQ3Q5Y3Q5g4xRoAHAAeACAAYkBiAGJAZIBAzAuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwj03fyQgYzuAhVC83MBHeJCB6kQ4dUDCAc&uact=5")
        elif "youtube" in query:
            query=query.replace("play","")
            query=query.replace("youtube","")
            query=query.replace("song","")
            try:
                speak(f"Playing {query} youtube")
                from youtube_search import YoutubeSearch
                results = YoutubeSearch(f"{query}", max_results=1).to_dict()
                res = results[0]['url_suffix']
                wb.get().open(f"https://youtube.com{res}")
            except Exception as e:
                print(e)
                speak("Sorry sir. Error delected.")
        elif "sing a song" in query:
            speak("Here is a song for you...")
            l = ["""
Before we eat, we wash, wash our hands,
Before we eat we wash, wash our hands,
We play, play, play, then we wash the germs away 
Before we eat, we wash, wash, wash our hands.
        ""","""
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.
            ""","""
oh ohh ohh. my personall, 
my personal ohhmy personal assistant,
we can work at the office late,
take long lunch breaks.
wont you be?
my personal assistant,
i dont mind givin you a raise,
all your vacations are paid,
wont you be?
my personal assistant,
yea,you have your own company car,
a parking space in the front,
so you dont have to walk far.
my personal assistant,
oh, a bonus,well thats me.
&& im given year-round
so wont you please"""]
            i = random.choice(l)
            speak2(i)
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
            python="F:\\Downloads\\Python apps"
            os.startfile(python)
        elif "watch hollywood movies" in query:
            movie_dir="E:\\"
            os.startfile(movie_dir)
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
            tekken="F:\\Downloads\\PPSSPP FOR WINDOWS\\PPSSPPWindows64.exe"
            os.startfile(tekken)
        elif "hub" in query:
            wb.get().open("https://github.com")
        elif "geeks for geeks" in query:
            wb.get().open("https://www.geeksforgeeks.com")
        elif "geeksforgeeks" in query:
            wb.get().open("https://www.geeksforgeeks.org")
        # elif "hub" in query:
        #     wb.get().open("https://github.com/new")
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
            wb.get().open("https://www.google.com/search?rlz=1C1CHBF_enIN930IN930&sxsrf=ALeKk021OBu5Mi4FeORt8nNSRLa97wPnIg%3A1610454856797&ei=SJf9X9qRMPKF4t4PtJ2x4AY&q=weather&oq=weather&gs_lcp=CgZwc3ktYWIQAzIMCCMQJxCdAhBGEIACMgUIABCRAjINCAAQsQMQgwEQFBCHAjIKCAAQsQMQgwEQQzIECAAQQzIECAAQQzIECAAQQzIKCAAQsQMQgwEQQzIECAAQQzICCAA6BwgjEOoCECc6CQgjECcQRhD_AToECCMQJzoHCCMQJxCdAlCMRVjgV2C4WWgBcAF4AYAB2wSIAcUNkgEJMC4zLjMuNS0xmAEAoAEBqgEHZ3dzLXdperABCsABAQ&sclient=psy-ab&ved=0ahUKEwja1ants5buAhXygtgFHbRODGwQ4dUDCA0&uact=5")
        elif "send email" in query:
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
            ppsspp="F:\\Downloads\\PPSSPP FOR WINDOWS\\PPSSPPWindows64.exe"
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
            python123="C:\\Users\\Naman Sharma\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib\\idle.pyw"
            os.startfile(python123)
        elif "onenote" in query:
            onenote="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\OneNote 2013"
            speak("opening. onenote")
            os.startfile(onenote)
        elif "infopath designer" in query:
            visio="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\InfoPath Designer 2013"
            speak("opening. visio")
            os.startfile(visio)
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
        elif "news" in query:
            data = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=ee17e6af8f6143f2af8758e2d2483dad").text
            # print(data.text)
            data = json.loads(data)
            news = data['articles']
            speak("Today's good news...")
            for n1,n in enumerate(news):
                # print(n['title'])
                speak(n['title'])
                if n1!=38:    
                    speak("Moving on to the next news.")
                elif n1==38:
                    speak("News Ended. Thanks for listening...")

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
        elif "dragon" in query:
            speak("Opening. Electro dragon adventures")
            idr = "F:\\Downloads\\Dragon Game\\Main.py"
            os.startfile(idr)
        elif "bye" in query:
            speak("Quitting sir. Thanks for the time.")
            root.destroy()
        elif "exit" in query:
            speak("Exitting sir... Thanks for the time.")
            root.destroy()
        elif "clock" in query:
            speak("Opening... Clock")
            os.startfile("F:\\downloads\\Python apps\\Dist\\Clock.exe")
        elif "site" in query:
            query=query.replace("site","")
            query=query.replace("open","")
            query=query.replace("webpage","")
            speak("Opening... webpage")
            # print(search(f"{query}"))
            wb.get().open(search(f"{query}")[0])
            
        else:
            speak("These results are back from a search...")
            wb.get().open(f"https://www.google.com/search?sxsrf=ALeKk002Ym5y6AR87ae1uuTTMcsBsMz3og%3A1610097643995&source=hp&ei=6yP4X7S8OsLmz7sP4oWdyAo&q={query}&oq={query}&gs_lcp=CgZwc3ktYWIQAzIHCC8MQyQMQJzIECCMQJzIECCMQJzIECAAQQzIHCAAQsQMQQzIECAAQQzIECAAQQzIKCC4QxwEQowIQQzIICAAQsQMQgwEyBAgAEENQ3Q5Y3Q5g4xRoAHAAeACAAYkBiAGJAZIBAzAuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwj03fyQgYzuAhVC83MBHeJCB6kQ4dUDCAc&uact=5")
        # root.update_idletasks()
root.update()    
Button(root, image=photo, command=main).place(x = 300, y = 240)
root.mainloop()
''' 
this is the end....
for the code...
but code will be update day by day...
'''
