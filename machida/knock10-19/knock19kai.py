# -*- coding: utf-8 -*-
from collections import defaultdict

f = open('hightemp.txt')
txt = f.readlines()
f.close()
dic = defaultdict(list)
lit = list(map(lambda x:x.split('\t')[0], txt))

for (i, l) in enumerate(lit):
    dic[l].append(i)
for d in reversed(sorted(dic.items(), key=lambda x:len(x[1]))):
    for i in d[1]:
        print(txt[i], end='')
