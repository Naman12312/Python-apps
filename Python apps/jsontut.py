import json
data = '{"var1":"Harry", "var2":56}'
print(data)
parsed = json.loads(data)
print(type(parsed))



data2 = {
    "Channel_Name":"CodeWithHarry",
    "Cars":['BMW','Audi a8', 'Ferrari'],
    "Fridge":('roti', 540),
    "isBad":False
}

jscomp = json.dumps(data2)
print(jscomp)