#acending
import sys
import os

print("give me 3 number")
our_list=[]
for z in range(3):
    num=int(input())
    our_list.append(num)

for x in range(2):
    if(our_list[x] < our_list[x+1]):
       print("this is OK")
    else:
        
        a=our_list[0]
        our_list[0]=our_list[1]
        our_list[1]=a
        c=our_list[2]
        our_list[2]=our_list[1]
        our_list[1]=c




        our_list[2]=a
        
       
       

print(our_list)
