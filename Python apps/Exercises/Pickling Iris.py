import requests
import pickle
r = requests.post("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
# Spliting the data
data = r.text.split()
# making a list of list
l = [d.split() for d in data]
# pickling the list
f = open("data.pkl", "wb")
a = pickle.dump(l, f)
f.close()
# Reading the list
f = open("data.pkl", "rb")
j = pickle.load(f)
print(j)
f.close()
