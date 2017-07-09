import gzip
import json
import pymongo
from pymongo import MongoClient

def insert_mongo(artists):
	client = MongoClient()
	db = client.testdb
	collection = db.artist
	
	collection.insert_many(artists)
	
	collection.create_index([('name', pymongo.ASCENDING)])  
	collection.create_index([('aliases.name', pymongo.ASCENDING)])  
	collection.create_index([('tags.value', pymongo.ASCENDING)])
	collection.create_index([('rating.value', pymongo.ASCENDING)])


def read_artist():
	with gzip.open("artist.json.gz", "r") as f:
		ret = []
		for line in f:
			data_json = json.loads(line)
			ret.append(data_json)
		return ret

if __name__ == '__main__':
	artists = read_artist()
	insert_mongo(artists)


	# collection.insert_many([{'a':12},{'B':6}])