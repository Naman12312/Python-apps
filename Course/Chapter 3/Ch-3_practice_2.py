letter = '''Dear <|NAME|>, 

You are selected!

Date: <|DATE|>
'''
name = input("Enter Your Name:\t")
Date = input("Enter Date:\t")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", Date)
print(letter)