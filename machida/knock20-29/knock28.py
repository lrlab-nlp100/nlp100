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
    ref1 = re.compile(r'<ref>(.*?)</ref>', re.DOTALL)
    ref2 = re.compile(r'<ref(.*?)(/>|>)')
    br = re.compile(r'<br\s*/>')

    for l in lit:
        s = enhance.sub('', l[1])
        s = link.sub(r'\1', s)
        s = ref1.sub(r'\1', s)
        s = ref2.sub(r'\1', s)
        s = br.sub('', s)
        dic[l[0]] = s

    for k, v in dic.items():
        print(k + ':' + v)
