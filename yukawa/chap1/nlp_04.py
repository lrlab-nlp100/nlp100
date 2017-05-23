# -*- coding: utf-8 -*-

import re
s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
l = filter(lambda w:len(w)>0,re.split(r"\s|\.|,",s))
first = [1,5,6,7,8,9,15,16,19]
d = {}
i = 1
for word in l:
    if i in first:
        d.update({i:word[0:1]})
    else:
        d.update({i:word[0:2]})
    i += 1
print(d)
