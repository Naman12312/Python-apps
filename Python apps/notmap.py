a = [1,2,3,4,5]
# without map
# for index, i in enumerate(a):
#     a[index] = i**2

# print(a)


# with map
def main(i):
    return i**2
a = map(main, a)
a = list(a)
print(a)



# map is more convenient