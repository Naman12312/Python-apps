import time
import webbrowser
import random
import string

#First pip install random-word
import requests
x = 0
alpha = string.ascii_letters + string.digits




time.sleep(3)
for i in range(0,30):
    webbrowser.open(f"http://www.bing.com/search?q={alpha}")