# -*- coding: utf-8 -*-

import re
s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
l = filter(lambda w:len(w)>0,re.split(r"\s|\.|,",s))
res = []
for word in l:
    res.append(len(word))
print(res)
