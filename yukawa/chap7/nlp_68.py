# -*- coding: utf-8 -*-
import plyvel
import pymongo
client = pymongo.MongoClient()
db = client['my_database']
col = db.my_collection
l = list(col.find({'tags.value':'dance'}).sort('rating.count',-1).limit(10))
for cont in l:
    print(cont)
