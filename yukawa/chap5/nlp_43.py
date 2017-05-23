# -*- coding: utf-8 -*-
import nlp_41
l = nlp_41.make_chunk()
for s in l:
    for c in s:
    	if c.is_ntov(s[c.dst]) and c.dst != -1:
            text = []
            text.append(c.mtoc(c)+'\t')
            text.append(c.mtoc(s[c.dst]))
       	    print(''.join(text))
