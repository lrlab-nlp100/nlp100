# -*- coding: utf-8 -*-
import nlp_30
from numpy import *
import matplotlib.pyplot as plt
from collections import Counter
l = nlp_30.read()
s_l = []
for line in l:
    for word in line:
        s_l.append(word['surface'])
counter = Counter(s_l)
high = []
for word,cnt in counter.most_common():
    high.append(cnt)
plt.xscale('log')
plt.yscale('log')
plt.plot(range(1,len(high)+1),high,'bo',markersize=3)
plt.show()
