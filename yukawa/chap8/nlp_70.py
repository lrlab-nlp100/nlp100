# -*- coding: utf-8 -*-
import random
l = []
with open('rt-polaritydata/rt-polaritydata/rt-polarity.neg','r',encoding='latin1') as neg,open('rt-polaritydata/rt-polaritydata/rt-polarity.pos','r',encoding='latin1') as pos:
    for line in neg:
        line = '-1 '+line
        l.append(line)
    for li in pos:
        li = '+1 '+li
        l.append(li)
random.shuffle(l)
with open('sentiment.txt','w') as out:
    for i in l:
        out.write(i)
with open('sentiment.txt','r') as s:
    p,n = 0,0
    for line in s:
        if '+1' in line:
            p += 1
        elif '-1' in line:
            n += 1
print(p,n)
