# -*- coding: utf-8 -*-

import re
def make_gram(n,s):
    gram = []
    for i in range(0,len(s)-1):
        gram.append(s[i:i+n])
    return gram

s = "I am an NLPer"
l = s.split()
print(make_gram(2,s))
print(make_gram(2,l))
