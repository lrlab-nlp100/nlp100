# -*- coding:utf-8 -*-
from knock30 import mload

ml = mload()
n_comb = []
n = []
for m in ml:
    for dic in m:
        if dic['pos'] == '名詞':
            n.append(dic['surface'])
        else:
            if len(n) > 1:
                n_comb.append(''.join(n))
            n = []

print(n_comb)
