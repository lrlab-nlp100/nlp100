# -*- coding: utf-8 -*-
import nlp_41
l = nlp_41.make_chunk()
text = []
for s in l:
    for c in s:
        if len(c.srcs) != 0: 
            verb = []
            jo = []
            jo_c = []
            if c.verb() is not None:
                verb.append(c.verb())
            for i in c.srcs:
                if s[int(i)].jo('') is not None:
                    jo.append(s[int(i)].jo(''))
                    jo.append(' ')
                    jo_c.append(s[int(i)].jo('chunk'))
                    jo_c.append(' ')
            if len(jo) != 0 and len(verb) != 0:
                jo.append('\t')
                verb.append('\t')
                jo_c.append('\n')
                text.append(''.join(verb)+''.join(jo)+''.join(jo_c))
print(''.join(text))
