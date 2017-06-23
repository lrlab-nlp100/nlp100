# -*- coding:utf-8 -*-
from knock30 import mload

ml = mload()
n_phrase = []
for m in ml:
    if len(m) < 3:
        continue
    for i in range(1, len(m)-1):
        if m[i]['surface'] == 'の':
            if m[i-1]['pos'] == '名詞' and m[i+1]['pos'] == '名詞':
                n_phrase.append(m[i-1]['surface'] + 'の' + m[i+1]['surface'])

print(n_phrase)
