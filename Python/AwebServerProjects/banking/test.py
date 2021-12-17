import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["bank"]
mycol = mydb["bank"]

myquery = { "address": "gg" }

mydoc = mycol.find(myquery)
for data in mydoc:
  print(data)