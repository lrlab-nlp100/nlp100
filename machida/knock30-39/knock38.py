# -*- coding:utf-8 -*-
from knock30 import mload
from collections import Counter
import matplotlib.pyplot as plt

ml = mload()
cnt = Counter([dic['surface'] for m in ml for dic in m])
freq = []
for k, v in cnt.most_common():
    freq.append(v)

plt.hist(freq, bins=200)
plt.xlabel('出現頻度')
plt.ylabel('単語の種類数')
plt.show()
