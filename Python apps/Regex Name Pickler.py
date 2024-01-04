# import requests
# a = requests.post("")
# Basic imports for the program...
import re
import pickle
# Making the string...
st = """

jkfgnjkgd
fkgdflgdf
Naman@Sharma
Mayany@Verma

fhgf
this
that 
df
g
fdfg
g
dgdf
fggdfgfd
df
dgf
f
g
dffg
g
dfg
gdfgdf
Punya@sorout
hjfiljf
f
f

f
ff

f
f
fffff
Vaibhav@sorout
main
fdgdf
fgd

gf
gf
gfgf
gfdfgdf
Manish@Sorout
Tripti@Sharma
"""
# Finding...
data = re.compile(r"\w+@+\S+\w")
matches = data.findall(st)
l = [mm.split() for mm in matches]
# print(l)
# Pickling...
f = open("author.pkl", "wb")
pickle.dump(l, f)
f.close()
f = open("author.pkl", "rb")
a = pickle.load(f)
print(a)
f.close()