# -*- coding: utf-8 -*-
import knock41

sentences = knock41.sentences
dic, lit = {}, []
for sentence in sentences:
    for s in sentence:
        if s.srcs != -1 and s.pos_is_noun_s() and sentence[s.srcs].pos_is_verb():
            key = s.s_phrase() + 'を' + sentence[s.srcs].first_verb()
            dic[key] = []
            noun_s_dst = s.dst
            verb_dst = sentence[s.srcs].dst
            for ss in sentence:
                if ss.dst != noun_s_dst:
                    if ss.srcs == verb_dst and ss.pos_is_post():
                        dic[key].append((ss.last_post(), ss.rm_symbol_phrase()))
            if len(dic[key]) == 0:
                dic = {}
                continue
    lit.append(dic)
    dic = {}

for l in lit:
        for k, v in l.items():
            print(k + '\t' + ' '.join([x[0] for x in sorted(v)]) + '\t' + ' '.join([x[1] for x in sorted(v)]))
