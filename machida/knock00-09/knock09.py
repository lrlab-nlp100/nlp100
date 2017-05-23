# -*- coding: utf-8 -*-
import random

def Typoglycemia(str):
    res = []
    for s in str.split(" "):
        if len(s) > 4:
            li = list(s[1:-1])
            random.shuffle(li)
            rand = s[0] + "".join(li) + s[-1]
            res.append(rand)
        else:
            res.append(s)
    return " ".join(res)

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print(Typoglycemia(str))
