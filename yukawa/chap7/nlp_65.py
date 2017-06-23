# -*- coding: utf-8 -*-
import plyvel
import pymongo
client = pymongo.MongoClient()
db = client['my_database']
col = db.my_collection
print(list(col.find({'name':'Queen'})))

# use my_database
# db.my_collection.find({name:'Queen'})

