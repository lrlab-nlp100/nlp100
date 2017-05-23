# -*- coding: utf-8 -*-
from knock05 import ngramc

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(ngramc(str1, 2))
Y = set(ngramc(str2, 2))

uni = X.union(Y)
inter = X.intersection(Y)
diff = X.difference(Y)

print("union", end="")
print(uni)
print("intersection", end="")
print(inter)
print("difference", end="")
print(diff)
print("'se' is %s" % uni.issuperset(['se']))
