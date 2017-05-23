# -*- coding:utf-8 -*-
import json, re

with open('uk.json', 'r') as f:
    lod = json.load(f)
    text = lod['text'].split('\n')
    for t in text:
        m = re.search('(File|ファイル):(.*?)\|', t)
        if m:
            print(m.group(2))
