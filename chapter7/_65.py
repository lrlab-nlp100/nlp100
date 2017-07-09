# db.artist.find({name:'Queen'})

import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.testdb
collection = db.artist

queen = collection.find({'name':'Queen'})
print(list(queen))