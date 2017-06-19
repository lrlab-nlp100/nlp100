# -*- coding: utf-8 -*-
import plyvel
import re
import gzip
import json
my_db = plyvel.DB('/Users/haraita/Documents/Program/nlp.ldb',create_if_missing=True)
with gzip.open('artist.json.gz','r') as f:
    for line in f:
        json_str = line.decode('utf-8')
        obj = json.loads(json_str)
        if 'name' in obj and 'area' in obj:
            my_db.put(obj['name'].encode('utf-8'),obj['area'].encode('utf-8'))
my_db.close()
