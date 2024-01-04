import pickle
# Pickling or achhaaarr banaaanaa... a python object...
cars = ["audi", "BMW", "mercedes"]
file = "mycar.pkl"
fileobj = open(file, "wb")
pickle.dump(cars, fileobj)
fileobj.close()
file = "mycar.pkl"
fileobj = open(file, "rb")
mycar = pickle.load(fileobj)
print(mycar)

