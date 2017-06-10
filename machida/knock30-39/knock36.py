# -*- coding:utf-8 -*-
from knock30 import mload
from collections import defaultdict

ml = mload()
cnt = defaultdict(int)
for m in ml:
    for dic in m:
        cnt[dic['surface']] += 1

for k,v in reversed(sorted(cnt.items(), key=lambda x: x[1])):
    print(k + ':' + str(v))
