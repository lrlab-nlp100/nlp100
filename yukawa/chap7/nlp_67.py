# -*- coding: utf-8 -*-
import pymongo
client = pymongo.MongoClient()
db = client['my_database']
col = db.my_collection
print(list(col.find({'aliases.name':'オアシス'})))
