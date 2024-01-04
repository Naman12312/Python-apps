import requests
# import json
from plyer import notification
import time
def notfyme(title, msg):
    notification.notify(
        title = title,
        message = msg,
        app_icon = None,
        timeout = 10
    )
# r = requests.get("https://covid19.who.int/WHO-COVID-19-global-table-data.csv").text
# print(r[720:743], end=" ")
while True:
    r = requests.get("https://covid19.who.int/WHO-COVID-19-global-table-data.csv").text
    notfyme("Covid-19 status in india: ", f"{r[743:783]}")
    time.sleep(3600)
