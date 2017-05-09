# -*- coding: utf-8 -*-
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
str1 = "パトカー"
str2 = "タクシー"

res = ""
for (s1, s2) in zip(str1, str2):
    res = res + s1 + s2

print(res)
