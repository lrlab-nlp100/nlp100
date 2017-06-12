# -*- coding:utf-8 -*-
from knock30 import mload

ml = mload()
n_surface = []
for m in ml:
    for dic in m:
        if dic['pos1'] == 'サ変接続':
            n_surface.append(dic['surface'])

print(n_surface)
