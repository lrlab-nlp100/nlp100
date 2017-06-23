# -*- coding: utf-8 -*-
import re
pa = re.compile(r'<word>(.+)</word>')
with open('nlp.txt.xml','r') as f:
    for line in f:
        word = pa.search(line)
        if word is not None:
            print(word.group(1))

