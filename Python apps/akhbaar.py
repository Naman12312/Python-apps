import requests
import json
data = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=ee17e6af8f6143f2af8758e2d2483dad").text
# print(data.text)
data = json.loads(data)
for index,i in enumerate(data['articles']):
    if index!=10:

        news = i['title']+ " - " + i['source']['name']
        print(news)
        print()
    