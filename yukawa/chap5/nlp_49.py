# -*- coding: utf-8 -*-
import nlp_41


l = nlp_41.make_chunk()
for s in l:
    for i,c in enumerate(s):
        if c.is_noun():
            for j,c in enumerate(s):
                if c.is_noun() and i != j:

