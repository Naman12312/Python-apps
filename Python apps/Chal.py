input1=int(input("तुम्हारी उम्र क्या है?\n"))
if input1>18 and input1<100:
    print("तुम सब चला सकते हो")
elif input1==18:
    print("हम तुम्हारा टेस्ट लेंगे")
elif input1==100 or input1>70:
    print("तुम पागल मत बनाओ")
else:
    print("बेटा तुम कुछ मत चलाओ")