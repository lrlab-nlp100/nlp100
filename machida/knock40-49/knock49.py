# -*- coding: utf-8 -*-
import knock41

sentences = knock41.sentences
lit, path, path2 = [], [], []
for sentence in sentences:
    for s in sentence:
        if s.srcs != -1 and s.pos_is_noun():
            for ss in sentence[s.dst+1:]:
                if ss.pos_is_noun():
                    noun_path = s.srcs
                    path.append(s.rep_noun('X'))
                    noun_path2 = ss.srcs
                    while True:
                        path.append(sentence[noun_path].rm_symbol_phrase())
                        if sentence[noun_path].dst == ss.dst:
                            path[-1] = 'Y'
                            lit.append((path, path2))
                            path, path2 = [], []
                            break
                        if sentence[noun_path].srcs == -1:
                            path2.append(ss.rep_noun('Y'))
                            while True:
                                path2.append(sentence[noun_path2].rm_symbol_phrase())
                                if sentence[noun_path2].srcs == -1:
                                    break
                                noun_path2 = sentence[noun_path2].srcs
                            lit.append((path, path2))
                            path, path2 = [], []
                            break
                        else:
                            noun_path = sentence[noun_path].srcs
for l in lit:
    if len(l[1]) != 0:
        print(' -> '.join(l[0][:-1]) + ' | ' + ' -> '.join(l[1][:-1]) + ' | '+ l[0][-1])
    else:
        print(' -> '.join(l[0]))
