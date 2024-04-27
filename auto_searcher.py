import webbrowser
import random
alphabet:tuple = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
numbers:tuple = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
total = (alphabet, numbers)
query:str = ""
for i in range(10):
    for i in range(5):
        query = query+random.choice(random.choice(total))
    print(query)
    webbrowser.open(f"https://www.bing.com/search?q={query}&form=QBLH&sp=-1&ghc=1&lq=0&pq=hrl&sc=11-3&qs=n&sk=&cvid=C4607A4FC3774E808B9D372908D4695F&ghsh=0&ghacc=0&ghpl=")
    query = ""
