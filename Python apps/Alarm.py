import time
import pyttsx3
import datetime
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice",voices[0].id)
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
Set_alarm = input("Set the alarm as Hour:Minute:Second\t")


work_to_do = input("Enter the work you want to do at the time you have set:\t")
current_time = datetime.datetime.now().strftime("%H:%M:%S")
while current_time != Set_alarm:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"The time is {current_time}")
    time.sleep(1)
if current_time == Set_alarm:
    for i in range(0, 5):    
        speak(f"Time to {work_to_do}")
