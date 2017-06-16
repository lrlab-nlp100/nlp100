# -*- coding: utf-8 -*-
import re
with open('enwiki-20150112-400-r10-105752.txt','r') as f,open('corpus.txt','w') as g:
    for line in f:
        l = re.split(' ',line)
        for i,word in enumerate(l):
            l[i] = re.sub(r'[.,!?;:\(\)\[\]\'\"]','',word)
            if len(l[i]) == 0:
                l.remove(l[i])
        line = ' '.join(l)
        g.write(line)
