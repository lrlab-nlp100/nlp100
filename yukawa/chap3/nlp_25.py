# -*- coding: utf-8 -*-
import re
with open('English.txt','r') as f:
    s = ''.join(f.readlines())
    a = re.search(u'基礎情報.*\n\|',s)
    b = re.search(r'[}]+\n',s[a.start():])
    l = re.split(u'\n[\|]+',s[a.end():a.start()+b.start()-1])
    d = {}
    for word in l:
        field = re.search(r'(.*?)(?=\s=)',word)
        value = re.search(r'(?<=\s=\s)(.*)',word)
        d.update({word[:field.end()]:word[value.start():]})
print(d)
