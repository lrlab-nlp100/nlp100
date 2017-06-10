# -*- coding:utf-8 -*-
import json, re
import requests

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

    url = 'http://ja.wikipedia.org/w/api.php?'
    param ={
        'format' : 'json',
        'action' : 'query',
        'prop' : 'imageinfo',
        'titles' : 'File:' + dic['国旗画像'],
        'iiprop' : 'url'}
    res = requests.get(url, params=param).json()
    image_url = res['query']['pages']['-1']['imageinfo'][0]['url']
    print(image_url)
