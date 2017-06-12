# -*- coding:utf-8 -*-
import json, re

with open('uk.json', 'r') as f:
    lod = json.load(f)
    text = lod['text']
    m = re.search(r'\{\{基礎情報\s国(.*?)\n\}\}\n', text, re.DOTALL)
    text = m.group(1)
    dic = {}
    lit = re.findall(r'\n\|(.*?)\s=\s(((?!\n\|).)*)', text, re.DOTALL)
    for l in lit:
        dic[l[0]] = l[1]
    print(dic)
