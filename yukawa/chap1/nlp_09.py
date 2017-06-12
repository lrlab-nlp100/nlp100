# -*- coding: utf-8 -*-

import random
s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
l = s.split()
res = ""
for word in l:
    if len(word) > 4:
        tmp = list(word[1:len(word)-1])
        #tmp = list(word[1:-1])
        ret = random.sample(tmp,len(word)-2)
        #ret = random.sample(tmp,len(tmp))
        w = word[0]
        w += ''.join(ret)
        w += word[len(word)-1]
        res += w
    else:
        res += word
    res += " "
print(s)
print(res)
