# Exersice Regex Email Collector solution:
import re
# Opening the text file in write mode:
f = open("emails.txt", "w")
f.write("")
st = """
my email id is Naman@gmail.com,
I have one more
email:"Naman@huri.com"
and some more
email :data@codewithharry.com;
email:::::;
Golia@gmail.com;
email:"pyuin@huri.com.in" and I have some more harry@codewithharry.com.
this are some 2 more emails: Naman@Codewithharry.com,
this is one more;
:::
gollaaa@gmail.com
1 surprise email:::::;
gotia@CodeWithHarry.com
gooooooooaaa@code.co.edu.in
"""
patt = re.compile(r"\w+@\S+\w+\w+")
matches = patt.finditer(st)
i = 1
# Finding the matches and writing to the file:
for match in matches:
    a = match.span()[0]
    b = match.span()[1]
    f.write(f"Email {i}: {st[a:b]}\n")
    i+=1
f.close()
# Reading the file and printing the emails:
f = open("emails.txt", "r")
for item in f.readlines():
    print(item)
f.close()
# Ending the program
