import requests
url = "https://api.ambeedata.com/weather/forecast/by-lat-lng"
querystring = {"lat":"12.9889055","lng":"77.574044","filter":"{hourly|minutely|daily}"}
headers = {
    'x-api-key': "39719d016bfdc67da80cd6c459871f10499fb41d73b0025aabdf0b40107ed959",
    'Content-type': "application/json"
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)

