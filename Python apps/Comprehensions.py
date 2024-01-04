# ls = []
# for i in range(0,100):
#     if i%3==0:
#         ls.append(i)
# ls = [i for i in range(0, 101) if i%3==0]
# print(ls)

# dict1 = {
#     i:f"item {i}" for i in range(0,1000000000) if i%1000==0
# }

# dict1 = {
#     i:f"item {i}" for i in range(0,6)
# }
# dict2 = {
#     value:item for item, value in dict1.items()
# }
# print(dict1, "\n", dict2)

# dresses = {dress for dress in ['dress1', 'dress2']}
# print(dresses)

# evens = (i for i in range(100) if i%2==0)
# for item in evens:    
#     print(item)
x = int(input("How many comprehensions you want???\t"))
x1 = input("Which type of comprehension you want???\nset comprehension\n list comprehension\n dictionary comprehension, press s, l, d respectively\t")
x = x+1
if x1=='s':
    s = {i for i in range(0, x)}
    print(s)
elif x1=="l":
    l = [i for i in range(0, x)]
    print(l)
else:
    d = {i:f"item {i}" for i in range(0,x)}
    print(d)