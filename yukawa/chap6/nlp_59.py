# -*- coding: utf-8 -*-
import re

def nest(s):
    cnt = 0
    num = 0
    for c in s:
        num += 1
        if c == ')':
            cnt -= 1
        elif c == '(':
            cnt += 1
        if cnt == 0:
            return s[:num]

pa = re.compile(r'<parse>(.+?)</parse>')
pa_NP = re.compile(r'\(NP')
pa_n = re.compile(r'\s([a-zA-Z\-\.\,]+?)\)')
with open('nlp.txt.xml','r') as f:
    for line in f:
        S = pa.search(line)
        if S is not None:
            NP_head = pa_NP.finditer(S.group(1))
            if NP_head is not None:
                for m in NP_head:
                    NP = nest(S.group(1)[m.start():])
                    word = pa_n.finditer(NP)
                    if word is not None:
                        for n in word:
                            if n.group(1) == '-LRB-':
                                print('( ',end="")
                            elif n.group(1) == '-RRB-':
                                print(') ',end="")
                            else:
                                print(n.group(1)+' ',end="")
                        print()
