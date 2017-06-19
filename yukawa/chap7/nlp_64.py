# -*- coding: utf-8 -*-
import pymongo
import gzip
import json
client = pymongo.MongoClient()
db = client.my_database
co = db.my_collection
with gzip.open('artist.json.gz','r') as f:
    for line in f:
        json_str = line.decode('utf-8')
        obj = json.loads(json_str)
        co.insert(obj)
co.create_index([("name",pymongo.ASCENDING)])
co.create_index([("aliases.name",pymongo.ASCENDING)])
co.create_index([("tags.value",pymongo.ASCENDING)])
co.create_index([("rating.value",pymongo.ASCENDING)])
