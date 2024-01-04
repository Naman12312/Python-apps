# def searcher():
#     import time
#     book = "This is a book on Harry and CodeWithHarry and good."
#     time.sleep(4)
#     while True:
#         text = (yield)
#         if text in book:
#             print("Your text is in the book.")
#         else:
#             print("Your text is not in the book.")
# search = searcher()
# next(search)
# search.send("Harry")
# input("press any key...\t")
# search.send("Harry and")
def searcher():
    import time
    text = "GoldarmGang Harry Tripti Rohan Skillf Nuclear King"
    time.sleep(3)
    while True:
        t = (yield)
        if t in text:
            print("Your name is in the text.")
        else:
            print("Your name is not in the text.")
search = searcher()
print("Running next method...")
def g():
    next(search)
g()
while True:
    x = input("What is your name???\t")   
    search.send(x)
