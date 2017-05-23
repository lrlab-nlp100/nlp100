# -*- coding: utf-8 -*-
import nlp_41
l = nlp_41.make_chunk()
text = []
for s in l:
    for c in s:
        if c.is_ntov(s[c.dst],'サ変接続') and c.is_jo('を'):
            sub = []
            jo = []
            jo_c = []
            sub.append(c.mtoc(c))
            sub.append(s[c.dst].verb())
            for i in c.srcs:
                if s[int(i)].is_jo() is not None:
                    jo.append(s[int(i)].is_jo())
                    jo.append(' ')
                    jo_c.append(s[int(i)].jo())
                    jo_c.append(' ')
            for i in s[c.dst].srcs:
                if s[int(i)].is_jo() is not None and c != s[int(i)]:
                    jo.append(s[int(i)].is_jo())
                    jo.append(' ')
                    jo_c.append(s[int(i)].jo())
                    jo_c.append(' ')
            if len(jo) != 0 and len(sub) != 0:
                jo.append('\t')
                sub.append('\t')
                jo_c.append('\n')
                text.append(''.join(sub)+''.join(jo)+''.join(jo_c))
print(''.join(text))

