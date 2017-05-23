# -*- coding: utf-8 -*-
import nlp_30
l = nlp_30.read()
for line in l:
    for word in line:
        if word['pos'] == '名詞' and word['pos1'] == 'サ変接続':
            print(word['surface'])
