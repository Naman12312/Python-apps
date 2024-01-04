'''
this is jarvis made by naman sharma
no one can edit this code except naman sharma who is me
'''
import wikipedia #pip install wikipedia
import pyttsx3 #pip install pyttsx3
from pyttsx3.drivers import sapi5
import speech_recognition as sr #pip install speech_recognition
import os
import webbrowser as wb
import datetime as dt
import random
import smtplib
claaaas={'English':'https://us04web.zoom.us/j/5539880620?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09',
'Math':"https://us04web.zoom.us/j/5566339731?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09",
'Gk':'https://us04web.zoom.us/j/5539880620?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09',
'Hindi':'https://us04web.zoom.us/j/5419446487?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09',
'Sst':'https://us04web.zoom.us/j/5419446487?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09',
'Science':'https://us04web.zoom.us/j/4995676395?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09',
'Sanskrit':'https://us04web.zoom.us/j/4410645586?pwd=ZjBuQkthSTRDN1ZGcnBYdVB3UWlGdz09'}
# chromepath="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
x=random.randrange(1,21)
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishme():
    hour=int(dt.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<17:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("Hello. I am jarvis. please tell how may i help you???")
ids={"Naman":"subhashhodal808@gmail.com","Dhruv":"dhruv98110sharma@gmail.com","Arush":"gameloop2021@gmail.com"}
def takecom():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("recognizing.....")
        query=r.recognize_bing(audio,language='en-in')
        print(f"user said:{query}")
    except Exception as e:
        print("say that again please....")
        speak("say that again please.... ")
        return "None"
    return query
with open("F:\\home pc\\my pandrive data\\ACROBAT-7.0\\don't open its nessesary.txt",'r') as f:
    iff=f.read()
def sendemail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('subhashhodal808@gmail.com',iff)
    server.sendmail('subhashhodal808@gmail.com',to,content)
    server.close()
if __name__ == "__main__":
    wishme()
    while True:
        query=takecom().lower()
        if 'wikipedia' in query:
            print("searching wikipedia....")
            speak("searching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=5)
            speak("acording to wikipedia...")
            print(results)
            speak(results)
        elif "open google" in query:
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
        # elif "play music" in query:
        #     music_dir="F:\\home pc\\my pandrive data\\songs"
        #     songs=os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir,songs[8]))
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
            notepad="F:\\Downloads\\Python apps\\dist\\notepad\\notepad.exe"
            os.startfile(notepad)
        elif "open word pad" in query:
            wordpad="C:\\Windows\\write.exe"
            os.startfile(wordpad)
        elif "calculate" in query:
            c="F:\\Downloads\\Python apps\\prosee calculator.py"
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
            snake="F:\\Downloads\\Python apps\\dist\snake.exe"
            os.startfile(snake)
        elif "bye" in query:
            speak("ok. bye. meet you later")
            exit()
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
        elif "youtube" in query:
            query=query.replace("youtube","")
            speak(f"Playing{query} on youtube")
            wb.get().open(f"https://www.youtube.com/results?search_query={query}")
        elif "google" in query:
            query=query.replace("google","")
            print("according to google...")
            speak("according to google...")
            wb.get().open(f"https://www.google.com/search?sxsrf=ALeKk002Ym5y6AR87ae1uuTTMcsBsMz3og%3A1610097643995&source=hp&ei=6yP4X7S8OsLmz7sP4oWdyAo&q={query}&oq={query}&gs_lcp=CgZwc3ktYWIQAzIHCC8MQyQMQJzIECCMQJzIECCMQJzIECAAQQzIHCAAQsQMQQzIECAAQQzIECAAQQzIKCC4QxwEQowIQQzIICAAQsQMQgwEyBAgAEENQ3Q5Y3Q5g4xRoAHAAeACAAYkBiAGJAZIBAzAuMZgBAKABAaoBB2d3cy13aXo&sclient=psy-ab&ved=0ahUKEwj03fyQgYzuAhVC83MBHeJCB6kQ4dUDCAc&uact=5")
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
            print("According to bing...")
            speak("According to bing...")
            wb.get().open(f"https://www.bing.com/search?q={query}&form=QBLH&sp=-1&pq=&sc=0-0&qs=n&sk=&cvid=DE9D8F29B3A54984BDF7D3BA3CF327B2")
        elif "stack overflow" in query:
            query=query.replace("stack overflow","")
            print("According to stackoverflow...")
            speak("According to stackoverflow...")
            wb.get().open(f"https://stackoverflow.com/questions/tagged/{query}")
        elif "program is " in query:
            query=query.replace("programmiz","")
            print("According to programmiz")
            speak("According to programmiz")
            wb.get().open(f"https://www.programiz.com/search/{query}")
        elif "who are you" in query:
            wishme()
        elif "open tekken 6" in query:
            tekken="F:\\Downloads\\PPSSPP FOR WINDOWS\\PPSSPPWindows64.exe"
            os.startfile(tekken)
        elif "open hub" in query:
            wb.get().open("https://github.com")
        elif "hub" in query:
            wb.get().open("https://github.com/new")
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
                print("whom to send??")
                speak("whom to send??")
                print(ids.keys())
                Too=takecom()
                print("What should i say?")
                speak("What should i say?")
                Content=takecom()
                sendemail(ids[Too],Content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                print("I have to appologize for this.")
                speak("I have to appologize for this.")
                print("Sorry my friend Naman bhai. i am not able to send this email")
                speak("Sorry my friend Naman bhai. i am not able to send this email")
        elif "brainly" in query:
            print("According to brainly...")
            speak("According to brainly...")
            query=query.replace("brainly","")
            wb.get().open(f"https://brainly.in/app/ask?q={query}")
        elif "codewithharry" in query:
            print("ok...")
            speak("ok...")
            query=query.replace("codewithharry","")
            wb.get().open(f"https://codewithharry.com/videos/{query}")
        elif "ppsspp" in query:
            print("Opening ppsspp")
            speak("Opening ppsspp")
            ppsspp="F:\\Downloads\\PPSSPP FOR WINDOWS\\PPSSPPWindows64.exe"
            os.startfile(ppsspp)
        elif "rpcs3" in query:
            print("opening rpcs3")
            speak("opening rpcs3")
            rpcs3="F:\\Downloads\\rpcs3-v0.0.14-11579-3567c43f_win64\\rpcs3.exe"
            os.startfile(rpcs3)
        elif "onedrive" in query:
            print("opening. onedrive")
            speak("opening. onedrive")
            onedrive="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\SkyDrive Pro 2013"
            os.startfile(onedrive)
        elif "python" in query:
            print("opening. python")
            speak("opening. python")
            python123="C:\\Users\\Naman Sharma\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\idlelib\\idle.pyw"
            os.startfile(python123)
        elif "onenote" in query:
            onenote="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\OneNote 2013"
            print("opening. onenote")
            speak("opening. onenote")
            os.startfile(onenote)
        elif "infopath designer" in query:
            visio="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\InfoPath Designer 2013"
            print("opening. visio")
            speak("opening. visio")
            os.startfile(visio)
        elif "gmail" in query:
            wb.get().open("https://mail.google.com")
        elif "skype" in query:
            print("opening. skype.")
            speak("opening. skype.")
            skype="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Lync 2013"
            os.startfile(skype)
        # elif "project" in query:
        #     print("opening. project") 
        #     speak("opening. project")
        #     project="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\"
        #     os.startfile(project)
        elif "outlook" in query:
            print("opening. outlook")
            speak("opening. outlook")
            outlook="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office 2013\\Outlook 2013"
            os.startfile(outlook)
        elif "friend" in query:
            query=query.replace("friend","")
            print(f"{query} aapki dost nahi banega") 
            speak(f"{query} aapki dost nahi banega")
            speak("want to retry???")
            retry=takecom()
            if retry=="yes":
                print("retry karne se bhi kuch nahi hoga")
                speak("retry karne se bhi kuch nahi hoga")
            elif retry=="no":
                print("bahut achha kiya")
                speak("bahut achha kiya")
        elif "sticky notes" in query:
            sticky="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories"
            print("opening. sticky notes")
            speak("opening. sticky notes")
            os.startfile(sticky)    
        elif "say" in query:
            query=query.replace("say","")
            speak(f"{query}")
        elif "remind" in query:
            try:
                hour1 = int(dt.datetime.now().hour)
                print("What you want to set in reminder???")
                speak("What you want to set in reminder???")
                remind = takecom()
                speak(f"{remind} At what time????")
                timee=takecom()
                speak("Reminder set!!!") 
                timti = int(timee)
                print(timti)
                if timti<=hour1:
                    print(f"Time to {remind}!")
                    speak(f"Time to {remind}")
                    speak(f"Time to {remind}")
                    speak(f"Time to {remind}")
                    speak(f"Time to {remind}")
                    speak(f"Time to {remind}")
                    speak(f"Time to {remind}")
                    speak(f"Time to {remind}")
            except Exception as e:
                print(e)
                print("Sorry Naman error delected!")         
                speak("Sorry Naman. error delected!")         
''' 
this is the end....
for the code...
but code will be update day by day...
'''
