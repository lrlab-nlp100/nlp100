# -*- coding: utf-8 -*-
import nlp_30
l = nlp_30.read()
for line in l:
    for word in line:
        if word['pos'] == '動詞':
            print(word['surface'])

