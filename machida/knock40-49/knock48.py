# -*- coding: utf-8 -*-
import knock41

sentences = knock41.sentences
lit, path = [], []
for sentence in sentences:
    for s in sentence:
        if s.srcs != -1 and s.pos_is_noun():
            noun_path = s.srcs
            path.append(s.rm_symbol_phrase())
            while True:
                path.append(sentence[noun_path].rm_symbol_phrase())
                if sentence[noun_path].srcs == -1:
                    break
                noun_path = sentence[noun_path].srcs
            lit.append(path)
            path = []

for l in lit:
    print(' -> '.join(l))
