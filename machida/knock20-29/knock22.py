# -*- coding:utf-8 -*-
import json, re

with open('uk.json', 'r') as f:
    lod = json.load(f)
    text = lod['text'].split('\n')
    for t in text:
        m = re.match(r'\[\[Category:(.*)\]\]', t)
        if m:
            print(m.group(1))
