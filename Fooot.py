list1=[int,float,str,"Naman",11,"Tripti",2,"Sumit",55]
for item in list1:
    if str(item).isnumeric() and item>6:
        print(item)