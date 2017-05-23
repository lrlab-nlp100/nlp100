# -*- coding:utf-8 -*-
import json, re

with open('uk.json', 'r') as f:
    lod = json.load(f)
    text = lod['text']
    m = re.search('\{\{基礎情報\s国(.*?)\n\}\}\n', text, re.DOTALL)
    text = m.group(1)
    ff = open('a', 'w')
    ff.write(text)
    ff.close()
    # print(text)
    dic = {}
    m = re.findall('\n\|(.*?)\s=\s(?!\n\|)', text)
    # for t in text:
    #     m = re.search('\|(.*?)\s=\s(.*)', t)
    #     if m:
    #         print(m.group(1))
    #         dic[m.group(1)] = m.group(2)
    for mm in m:
        print(mm)
    # print(dic)
 # p_field = re.compile('\n\|(.+?)\s+=\s+(((?!\n\|).)*)', re.DOTALL)
