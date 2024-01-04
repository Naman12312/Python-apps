import requests
from bs4 import BeautifulSoup
# r = requests.get("https://www.mygov.in/corona-data/covid19-statewise-status/").text
def getdata(url):
    r = requests.get(url)
    return r.text
myhtmldata = getdata("https://www.mygov.in/corona-data/covid19-statewise-status/")


# print(r)