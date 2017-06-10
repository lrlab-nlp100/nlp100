# -*- coding:utf-8 -*-
from knock30 import mload
from collections import Counter
import matplotlib.pyplot as plt

ml = mload()
cnt = Counter([dic['surface'] for m in ml for dic in m])
freq = []
for k, v in cnt.most_common():
    freq.append(v)

plt.xscale('log')
plt.yscale('log')
plt.plot(freq, [i for i in range(len(freq))])
plt.xlabel('順位')
plt.ylabel('出現頻度')
plt.show()
