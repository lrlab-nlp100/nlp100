# -*- coding:utf-8 -*-
import json, re

with open('uk.json', 'r') as f:
    lod = json.load(f)
    text = lod['text']
    m = re.search(r'\{\{基礎情報\s国(.*?)\n\}\}\n', text, re.DOTALL)
    text = m.group(1)
    dic = {}
    lit = re.findall(r'\n\|(.*?)\s=\s(((?!\n\|).)*)', text, re.DOTALL)
    enhance = re.compile(r'\'{2,5}')
    link = re.compile(r'\[\[(.*?)\]\]')
    for l in lit:
        s = enhance.sub('', l[1])
        s = link.sub(r'\1', s)
        dic[l[0]] = s

    for k, v in dic.items():
        print(k + ':' + v)
