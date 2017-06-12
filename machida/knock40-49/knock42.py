# -*- coding:utf-8 -*-
import knock41

sentences = knock41.sentences
for sentence in sentences:
    for s in sentence:
            if s.srcs != -1:
                if s.rm_symbol_phrase() == '':
                    continue
                res = s.rm_symbol_phrase() + '\t' + sentence[s.srcs].rm_symbol_phrase()
                print(res)
# for s in sentences[99]:
#         if s.srcs != -1:
#             if s.rm_symbol_phrase() == '':
#                 continue
#             # print(type(s.rm_symbol_phrase()))
#             # print(sentences[99][s.srcs].rm_symbol_phrase())
#             res = s.rm_symbol_phrase() + '\t' + sentences[99][s.srcs].rm_symbol_phrase()
#             print(res)
