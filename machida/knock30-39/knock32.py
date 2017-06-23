# -*- coding:utf-8 -*-
from knock30 import mload

ml = mload()
v_base = []
for m in ml:
    for dic in m:
        if dic['pos'] == '動詞':
            v_base.append(dic['base'])

print(v_base)
