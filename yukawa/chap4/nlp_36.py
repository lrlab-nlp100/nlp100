# -*- coding: utf-8 -*-
import nlp_30
from collections import Counter
l = nlp_30.read()
s_l = []
for line in l:
    for word in line:
        s_l.append(word['surface'])
counter = Counter(s_l)
for word,cnt in counter.most_common():
    print(word,cnt)

