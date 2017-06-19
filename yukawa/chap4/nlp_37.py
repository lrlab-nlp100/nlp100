# -*- coding: utf-8 -*-
import nlp_30
from numpy import *
import matplotlib
import matplotlib.pyplot as plt
from collections import Counter
font = {'family':'YuGothic'}
matplotlib.rc('font',**font)
l = nlp_30.read()
s_l = []
for line in l:
    for word in line:
        s_l.append(word['surface'])
counter = Counter(s_l)
high = []
label = []
i = 0
for word,cnt in counter.most_common():
    if i > 9:
        break
    high.append(cnt)
    label.append(word)
    i += 1
print(high)
plt.bar(range(1,11),high)
plt.xticks(range(1,11),label)
plt.show()
