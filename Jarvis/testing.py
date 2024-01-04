import pickle
a = [2,4,5,5,7]
y = open("p.pkl", 'wb')
pickle.dump(a, y)
y.close()
y = open("p.pkl",'rb')
a = pickle.loads(y)
print(a)