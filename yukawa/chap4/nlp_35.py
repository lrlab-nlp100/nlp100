# -*- coding: utf-8 -*-
import nlp_30
l = nlp_30.read()
for line in l:
    cnt = 0
    noun = []
    for word in line:
        if word['pos'] == '名詞':
            noun.append(word['surface'])
            cnt += 1
        elif cnt != 0:
            if cnt > 1:
                print(''.join(noun))
                noun = []
                cnt = 0
            elif cnt == 1:
                cnt = 0
                noun = []
