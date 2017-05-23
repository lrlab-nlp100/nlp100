# -*- coding: utf-8 -*-
import nlp_41
def path(chunk,s):
    if chunk.dst != -1:
        return chunk.mtoc(chunk)+'->'+path(s[chunk.dst],s)
    else:
        return chunk.mtoc(chunk)

l = nlp_41.make_chunk()
for s in l:
    for c in s:
        if c.is_noun():
            res = path(c,s)
            print(res)
