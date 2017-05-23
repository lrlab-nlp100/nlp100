# -*- coding: utf-8 -*-
import re
with open('English.txt','r') as f:
    s = ''.join(f.readlines())
    for m in re.findall(r'(?<=\[\[File:)(.*?)\|',s):
        print(m)
    for m in re.findall(u'(?<=ファイル:)(.*?)\|',s):
        print(m)
