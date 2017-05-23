from collections import Counter
import re
import json
import gzip
with gzip.open('jawiki-country.json.gz','r') as f:
    for line in f:
        json_str = line.decode('utf-8')
        obj = json.loads(json_str)
        if obj['title'] == 'イギリス':
            En_str = obj['text']
            break;
with open('English.txt','w',encoding='utf-8') as g:
    g.write(En_str)
print(En_str)
