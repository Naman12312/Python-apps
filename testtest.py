
    r1=sr.Recognizer()
    with sr.Microphone() as source1:

        # print("listening....")
        # resl.set("listening....")
        r1.pause_threshold=0.9
        audio=r1.listen(source1)
        
    try:
       
        # print("recognizing.....")

        query1=r1.recognize_google(audio,language='en-in')
        print(query1)    
        if 'jarvis' in query1.lower():
            takecom()
    except Exception as e:
        pass