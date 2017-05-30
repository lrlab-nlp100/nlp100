# -*- coding: utf-8 -*-
import re
pa = re.compile(r'<word>(.+?)</word>')
p_ner = re.compile(r'<NER>(.+?)</NER>')
word = ''
with open('nlp.txt.xml','r') as f:
    for line in f:
        contents = pa.search(line)
        if contents is not None:
            word = contents.group(1)
        ner = p_ner.search(line)
        if ner is not None and ner.group(1) == 'PERSON':
            print(word)
