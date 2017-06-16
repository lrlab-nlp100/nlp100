# -*- coding: utf-8 -*-
from nltk.corpus import stopwords
import re
import nlp_71
from stemming.porter2 import stem
v = []
with open('sentiment.txt','r') as f:
    for line in f:
        l = list(filter(lambda w:len(w) > 0 and nlp_71.is_stop(w) is False,re.split('\s|"|,|\.|\'|\(|\)|\-\-|:|;',line)))
        l = list(map(stem,l))
        v.append(l)
with open('feature.txt','w') as g:
    for i in v:
        g.write(' '.join(i))
        g.write('\n')
