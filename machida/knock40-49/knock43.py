# -*- coding:utf-8 -*-
import knock41

sentences = knock41.sentences
for sentence in sentences:
    for s in sentence:
        if s.srcs != -1:
            if s.pos_is_noun() and sentence[s.srcs].pos_is_verb():
                res = s.rm_symbol_phrase() + '\t' + sentence[s.srcs].rm_symbol_phrase()
                print(res)
