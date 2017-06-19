# -*- coding: utf-8 -*-
import plyvel
import pymongo
client = pymongo.MongoClient()
db = client['my_database']
col = db.my_collection
print(col.find({'area':'Japan'}).count())

# use my_database
# db.my_collection.find({area:'Japan'}).count()
