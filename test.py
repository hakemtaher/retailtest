import json

f = open ('bus.json', "r")
data = json.loads(f.read())
for i in data :
    print (i["name"])