# -*- coding: utf-8 -*-
import knock41

sentences = knock41.sentences
dic, lit = {}, []
for sentence in sentences:
    for s in sentence:
        if s.srcs != -1 and s.pos_is_post() and sentence[s.srcs].pos_is_verb():
            if sentence[s.srcs].first_verb() in dic:
                dic[sentence[s.srcs].first_verb()].append((s.last_post(), s.rm_symbol_phrase()))
            else:
                dic[sentence[s.srcs].first_verb()] = []
                dic[sentence[s.srcs].first_verb()].append((s.last_post(), s.rm_symbol_phrase()))
    lit.append(dic)
    dic = {}

for l in lit:
        for k, v in l.items():
            print(k + '\t' + ' '.join([x[0] for x in sorted(v)]) + '\t' + ' '.join([x[1] for x in sorted(v)]))
