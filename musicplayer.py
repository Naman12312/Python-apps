import requests

url = "https://spotify23.p.rapidapi.com/search/"

querystring = {"q":"Blinding lights","type":"multi","offset":"0","limit":"10","numberOfTopResults":"5"}

headers = {
	"X-RapidAPI-Key": "28290b323fmshe033439f8e21c87p1d253cjsn9438d52a3d39",
	"X-RapidAPI-Host": "spotify23.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())