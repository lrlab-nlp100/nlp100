# -*- coding: utf-8 -*-
import nlp_30
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter
l = nlp_30.read()
s_l = []
for line in l:
    for word in line:
        s_l.append(word['surface'])
counter = Counter(s_l)
p = sorted(counter.items(),key=lambda x:x[1])
left = []
for i in p:
    left.append(i[1])
plt.hist(left,bins=50,range=(1,50))
plt.show()
