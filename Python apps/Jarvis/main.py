# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import speech_recognition as sr
import openai
import webbrowser as wb
import pyttsx3


def speak(query):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(query)
    engine.runAndWait()


def takecom():
    global resl
    global user

    r = sr.Recognizer()
    with sr.Microphone() as source:

        # resl.set("listening....")

        print("listening....")
        # resl.set("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:

        print("recognizing.....")

        query = r.recognize_google(audio)

        print(f"user: {query}\n")

        # user.set("")

    except Exception as e:
        # print(e)
        speak("Sorry, I can't hear you. say that again.")
        return "None"

    resl.set("recognizing.....")
    return query


while True:

    a = takecom().lower()

    OPENAI_API_KEY = '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'
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{
                                                "role":
                                                "system",
                                                "content":
                                                "You are a helpful assistant ."
                                            }, {
                                                "role": "user",
                                                "content": a
                                            }, {
                                                "role": "assistant",
                                                "content": a
                                            }, {
                                                "role": "user",
                                                "content": a
                                            }])
    print(response['choices'][0]['message']['content'])
