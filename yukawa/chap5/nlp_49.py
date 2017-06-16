# -*- coding: utf-8 -*-
import nlp_41
import re
ll = []
def path(chunk,s,x):
    ll.append(chunk.dst)
    if chunk.dst != -1 and len(ll) == 1:
        return chunk.mtoc_t(chunk,x)+'->'+path(s[chunk.dst],s,x)
    if chunk.dst != -1 and len(ll) > 1:
        return chunk.mtoc(chunk)+'->'+path(s[chunk.dst],s,x)
    else:
        return chunk.mtoc(chunk)

l = nlp_41.make_chunk()
for s in l:
    for i,c in enumerate(s):
        if c.is_noun():
            for j,d in enumerate(s):
                if d.is_noun() and i < j:
                    ret_i = path(c,s,'X')
                    l_i = ll
                    ll = []
                    ret_j = path(d,s,'Y')
                    l_j = ll
                    ll = []
                    word_d = d.mtoc(d)
                    li = re.split('\-\>',ret_i)
                    lj = re.split('\-\>',ret_j)
                    if word_d in li:
                        ind = li.index(word_d)
                        if ind > 0:
                            li[ind] = 'Y'
                            root = '->'.join(li[:ind+1])
                            print(root)
                    else:
                        y = list(set(l_i) & set(l_j))
                        for k in l_i:
                            if k in y:
                                print('->'.join(li[:li.index(s[k].mtoc(s[k]))])+'|'+'->'.join(lj[:lj.index(s[k].mtoc(s[k]))])+'|'+li[li.index(s[k].mtoc(s[k]))])
                                break

