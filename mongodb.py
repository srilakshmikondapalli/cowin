import pymongo
def mongo_connect():
    myclient=pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient["database"]
    mycol=mydb["student"]
    mydict=[{"first_name":"john","second_name":"smith"},{"first_name":"steve","second_name":"jobes"}]
    x=mycol.insert_many(mydict)
    print(x.inserted_ids)

mongo_connect()