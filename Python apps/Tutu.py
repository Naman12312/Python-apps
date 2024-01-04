
# Python program to find current
# weather details of any city
# using openweathermap api
import pyttsx3
engine =pyttsx3.init('sapi5')
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
# import required modules
import requests, json
 
# Enter your API key here
api_key = "7791613b400073e2417bbcc39e8869fd"
 
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
 
# Give city name
city_name = input("Enter city name : ")
 
# complete_url variable to store
# complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(complete_url).text
response = json.loads(response)
# print(response)
des = response["weather"][0]["description"]
tempp = response['main']["temp"]
tempp = tempp - 273.15
humidity = response['main']["humidity"]
print(f"City:{city_name}\n",
    f"Weather:{des}\n",
    f"Temperature: {int(tempp)} C\n",
    f"Humidity:{humidity}%\n")
speak(f"City{city_name}\n"+
    f"Weather{des}\n"+
    f"Temperature {int(tempp)} degree Celcius\n"+
    f"Humidity{humidity}%\n")