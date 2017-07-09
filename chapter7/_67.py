import pymongo
from pymongo import MongoClient

def searchByAlias(alias):
	client = MongoClient()
	db = client.testdb
	collection = db.artist

	return list(collection.find({'aliases.name':alias}))


if __name__ == '__main__':
	ans = searchByAlias('オアシス')
	print(ans)