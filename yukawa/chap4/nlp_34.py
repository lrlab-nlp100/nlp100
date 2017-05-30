# -*- coding: utf-8 -*-
import nlp_30
l = nlp_30.read()
for line in l:
    for i,word in enumerate(line):
        if i < len(line)-2 and word['pos'] == '名詞' and line[i+1]['surface'] == 'の' and line[i+2]['pos'] == '名詞':
            print(word['surface']+line[i+1]['surface']+line[i+2]['surface'])
