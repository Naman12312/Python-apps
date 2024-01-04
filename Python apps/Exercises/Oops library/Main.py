with open("G.txt", "w") as f:
    f.write("")
with open("Data.txt", "w") as f:
    f.write("")
class Library:
    input1 = input("What is Your Name???\t") 
    def g(self):
        xc = input("What is Your Name???\t") 
        with open("G.txt", "w") as f:
            f.write(self.input1)
        self.input1 = xc
    books = {
        "Science": "Available",
        "Math": "Available",
        "Hindi": "Available",
        "English" : "Available",
        "Gk": "Available",
        "History": "Available",
        "Geography": "Available",
        "Polilics" : "Available",
        
    }
    def __init__(self):
        self.books = Library.books
    def lend_book(self):   
        input2 = input(f"Which book you want???\t")
        book = self.books[input2]
        if book=="Available":
            print("This book is Available.")
            print("Read this and return after 1 week")
            self.books[input2]=f"{self.input1} Has this book."
            print(self.books[input2])
        elif book!="Available":
            print("This book is not Available.")
            f = open("G.txt", "r")
            print(f"{f.read()} has this book")
            print("You Can take this after he returns the book")
            f.close()
    def return_book(self):
        input3 = input("Which book you want to return???\t")
        self.books[input3] = "Available"
        print("Ok you can take a new book by lending a book.")
    def DBook(self):
        print(f"The Books Are:\n {self.books}")
    def addbo(self):
        x111 = input("Which Book you want to add???\t")
        self.books[x111] = "Available"
        print("Book Added!")
        print(self.books)
Harry = Library()
if __name__=="__main__":
    while True:
        x = input("""What do you want to do??? options are:
Lend Book,
Return Book,
Display book,
Add book

press l for lend book, r for return book, d for Display book, a for add book.
""")
        if x=="l":
            Harry.lend_book()
        elif x=="r":
            Harry.return_book()
        elif x=="d":
            Harry.DBook()
        elif x=="a":
            Harry.addbo()
        else:
            print("Paagal hai kya bhai???")
        Harry.g()