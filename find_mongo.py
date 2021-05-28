import pymongo
def mongo_connect():
    myclient=pymongo.MongoClient("mongodb://localhost:27017/")
    mydb=myclient["database"]
    mycol=mydb["student"]
    query={"second_name":"smith"}
    res=mycol.find(query)
    for x in res:
        print(x)

mongo_connect()