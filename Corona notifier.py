from plyer import notification
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
import time
def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "F:\\downloads\\icon.ico",
        timeout = 5

    )
def getdata(url):
    r = requests.get(url)
    return r.content
if __name__=="__main__":
    # notifyme("Corona","Naman lets stop the spread of covid-19")
    with open("text1.txt","w") as f:
        f.write('''	 
        '''
        )
    with open("text2.txt",'w') as f:
        f.write('''
Uttar Pradesh:	total: 6368	\nchange yesterday: 169 down	deaths: 8616 
Haryana:  total: 1254, \nchange yesterday: 30 down, deaths: 3014
        ''')
    with open("text1.txt","r") as r:
        d = r.read()
    with open("text2.txt","r") as r:
        s = r.read()
    while True:
        notifyme("Corona status in",s)
        time.sleep(3600)