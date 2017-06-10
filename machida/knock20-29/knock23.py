# -*- coding:utf-8 -*-
import json, re

with open('uk.json', 'r') as f:
    lod = json.load(f)
    text = lod['text'].split('\n')
    for t in text:
        m = re.match(r'(==+)\s*(.*?)\s*==+', t)
        if m:
            print(str(len(m.group(1))) + ':' + m.group(2))
