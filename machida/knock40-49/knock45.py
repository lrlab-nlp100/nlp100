# -*- coding: utf-8 -*-
import knock41

sentences = knock41.sentences
dic, lit = {}, []
for sentence in sentences:
    for s in sentence:
        if s.srcs != -1 and s.pos_is_post() and sentence[s.srcs].pos_is_verb():
            if sentence[s.srcs].first_verb() in dic:
                dic[sentence[s.srcs].first_verb()].append(s.last_post())
            else:
                dic[sentence[s.srcs].first_verb()] = []
                dic[sentence[s.srcs].first_verb()].append(s.last_post())
    lit.append(dic)
    dic = {}

for l in lit:
        for k, v in l.items():
            print(k + '\t' + ' '.join(sorted(v)))

# comannd
# sort knock45_result | uniq -c | sort -r | head -20
# cat knock45_result | grep '^する\t'| sort | uniq -c | sort -r | head -10
# cat knock45_result | grep '^見る\t'| sort | uniq -c | sort -r | head -10
# cat knock45_result | grep '^与える\t'| sort | uniq -c | sort -r | head -10
