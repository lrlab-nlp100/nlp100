import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.testdb
collection = db.artist

lst = list(collection.find({'tags.value':'dance'}).sort('rating.count',pymongo.DESCENDING).limit(10))

for i, l in enumerate(lst):
	print('No.{}:{}'.format(i+1,l['name']))