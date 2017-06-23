# -*- coding:utf-8 -*-
from knock30 import mload
from collections import Counter
import matplotlib.pyplot as plt

ml = mload()
cnt = Counter([dic['surface'] for m in ml for dic in m])
label, height = [], []
for k,v in cnt.most_common(10):
    label.append(k)
    height.append(v)

plt.bar([i for i in range(10)], height)
plt.xticks([i for i in range(10)] ,label)
plt.show()
