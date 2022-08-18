import pymongo

client = pymongo.MongoClient("mongodb+srv://Shivprasad:Shivpi99@shivprasad.bkgom.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database["shiv"]

#names = collection.find({"name" :"shivprasad"})
#for i in names:
    #print(i)

data = collection.find({"subject":{"$gt":"E"}})
for i in data:
    print(i)
#data = collection.find({"subject":{"$gt":"E"}}) - This will work when (case sensitive)