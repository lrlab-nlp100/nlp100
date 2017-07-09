import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.testdb
collection = db.artist

cnt = collection.find({'area':'Japan'}).count()

print(cnt)