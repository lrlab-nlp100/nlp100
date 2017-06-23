# -*- coding:utf-8 -*-
from knock30 import mload

ml = mload()
v_surface = []
for m in ml:
    for dic in m:
        if dic['pos'] == '動詞':
            v_surface.append(dic['surface'])

print(v_surface)
