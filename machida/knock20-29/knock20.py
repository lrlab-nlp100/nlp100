# -*- coding:utf-8 -*-
import json

with open('jawiki-country.json', 'r') as data:
    for d in data:
        lod = json.loads(d)
        if lod['title'] == 'イギリス':
            print(lod['text'])
            #21以降で使うデータをuk.jsonに保存しとく
            f = open('uk.json', 'w')
            f.write(json.dumps(lod, ensure_ascii=False, indent=4))
            f.close()
