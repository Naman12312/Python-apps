from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import speech_recognition as sr
import openai
from .models import Prompt
from django.forms.models import model_to_dict
import json
from gtts import gTTS
# from playsound import playsound
# import subprocess
from os import remove, system
import threading
import pywhatkit
# Create your views here.
# Plan:
# steps to make audioGPT in raspberry pi:
t = None
openai.api_key = "OPENAI_API_KEY"
def index(request):
    global t
    def speak2(txt):
        audio = gTTS(txt)
        audio.save("main2.wav")
        system('ffplay -nodisp -autoexit "D:\\drive D\\Downloads\\Python apps\\copilot\\GoldWriter\\main2.wav"')
    def speak(txt):
        audio = gTTS(txt)
        audio.save("main.wav")
        
        # speak code goes here
    def checkforedith():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
            with open("recording1.wav", "wb") as f:
                f.write(audio.get_wav_data())
            try:

                audio_file= open("recording1.wav", "rb")
                query = openai.Audio.transcribe("whisper-1", audio_file)
            except Exception as e:
                return "None"
            
            return query['text'].lower()
    def takecommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
            with open("recording1.wav", "wb") as f:
                f.write(audio.get_wav_data())
            try:

                audio_file= open("recording1.wav", "rb")
                query = openai.Audio.transcribe("whisper-1", audio_file)
                
            except Exception as e:
                speak("Say that again please...")
                return "None"
            
            return query['text'].lower()
        # takecommand code goes here

    check = checkforedith()
    if check=="chatgpt" or check=="chat gpt" or check=="edith":
        speak2("Yes?")
        a = takecommand() #Put takecommand() instead of this here
        # read data from database
        listofmsgsplus =  Prompt.objects.all().filter(role="user")
        listofmsgsplus = [model_to_dict(i) for i in listofmsgsplus]
        for i in listofmsgsplus:
            i.pop("id")
        # put into a list of prompts
        listofmsgs = [{"role":i['role'], "content":i['pro']} for i in listofmsgsplus]
        listofmsgs.append({"role":"user", "content":a})

        if a!="None":
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                                    messages=listofmsgs)
            listofmsgsplus.append({"role":"user", "pro":a, "response":response['choices'][0]['message']['content']})
            print(listofmsgsplus)
            #get the prompt from the html textarea
            db = Prompt(role = "user", pro=a, response = response['choices'][0]['message']['content'])
            db.save()
            # append the newest prompt to list of prompts
            

                


            #run ChatCompletions
            #write to the database
            # read data again from the database to include the newest prompt and response, and put it into a list of the messages
            #return the list [role:"user", prompt:f"{prompt}", response:f"{response}"...n times] as a json and read it from js
            #display on the page
            #speak the result
            
            t = threading.Thread(target=speak2, args=(response['choices'][0]['message']['content'],))
            t.start()
            return render(request, "index.html", {"main":json.dumps(listofmsgsplus)})
        else:
            
            return render(request, "index.html", {"main":
                                                  json.dumps([{"role":"user", "pro":"Couldn't hear properly", "response":"Say that again please..."}])} 
                                                )
        
    
    else:
        return render(request, "index.html", {"main":
                                                  json.dumps([{"role":"user", "pro":"Couldn't hear properly", "response":"Say that again please..."}])})


# After this is done, put this all in a raspberry pi and make it work in AR glasses.

def thread_status(request):
    global t
    if t is not None and t.is_alive():
        data = {'status': 'running'}
    else:
        data = {'status': 'finished'}
    return JsonResponse(data)
