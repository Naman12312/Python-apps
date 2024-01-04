f1 = open("naman.txt")
try:
    f = open("does2.txt")
    # for item in f.readlines():
    #     print(item)
except EOFError as e:
    print("EofError!")
except IOError as e:
    print("IOError!")
    # print("Error!")
else:
    print("This will run only when except is not running...")
finally:
    print("Run this anyway....")
    # f.close()
    f1.close()
print("Important stuff!")
"""
Next: Coroutines In Python | Python Tutorials For Absolute Beginners In Hindi #
"""
if __name__=='__main__':
    