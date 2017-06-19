# -*- coding: utf-8 -*-
import re
from collections import defaultdict
with open('corpus.txt','r+') as f, open('name.txt','r') as g:
    name = []
    for line in g:
        name.append(line[:-1])
    print(name)
    for line in f:
        for country in name:
            c_of_line = re.finditer(country,line)
            if c_of_line is not None:
                for m in c_of_line:
                    line = re.sub(line[m.start():m.end()],re.sub(u' ',u'_',line[m.start():m.end()]),line)
        f.write(line)
