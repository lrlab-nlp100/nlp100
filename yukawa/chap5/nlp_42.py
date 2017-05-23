# -*- coding: utf-8 -*-
import nlp_41
l = nlp_41.make_chunk()
for s in l:
    for c in s:
        if c.dst != -1 and len(c.morphs) != 0:
            text = []
            text.append(c.mtoc(c)+'\t')
            text.append(c.mtoc(s[c.dst]))
            print(''.join(text))
