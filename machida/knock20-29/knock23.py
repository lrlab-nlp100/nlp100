# -*- coding:utf-8 -*-
import json, re

with open('uk.json', 'r') as f:
    lod = json.load(f)
    text = lod['text'].split('\n')
    i = 1
    for t in text:
        m = re.match('==+\s*(.*?)\s*==+', t)
        if m:
            print(str(i) + ":" + m.group(1))
            i += 1
