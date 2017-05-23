# -*- coding: utf-8 -*-
import nlp_41
l = nlp_41.make_chunk()
text = []
for s in l:
    for c in s:
        if len(c.srcs) != 0: 
            verb = []
            jo = []
            if c.verb() is not None:
                verb.append(c.verb())
            for i in c.srcs:
                if s[int(i)].jo() is not None:
                    jo.append(s[int(i)].jo())
                    jo.append(' ')
            if len(jo) != 0 and len(verb) != 0:
                jo.append('\n')
                verb.append('\t')
                text.append(''.join(verb)+''.join(jo))
print(''.join(text))
