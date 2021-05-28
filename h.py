import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["database"]
mycol = mydb["student"]

for x in mycol.find():
  print(x)
