# -*- coding: utf-8 -*-
import re
with open('nlp.txt','r') as f:
    for line in f:
        for m in re.findall(r'[\.;:?!]\s[A-Z]',line):
            line = re.sub(m,re.sub(r'\s',r'\n',m),line)

        print(line)

