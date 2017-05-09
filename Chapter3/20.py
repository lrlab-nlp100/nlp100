# -*- coding: UTF-8 -*-
import json

with open('jawiki-country.json', 'r') as f:
    for line in f:
        Json_line=json.loads(line)
        if Json_line['title']=='イギリス':
            with open('uk.txt','w') as file:
                file.write(Json_line['text'])
    print()