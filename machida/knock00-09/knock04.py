# -*- coding: utf-8 -*-

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
num = [1, 5, 6, 7, 8, 9, 15, 16, 19]

dic = {}
for (i, s) in enumerate(str.split(" "), start=1):
    if i in num:
        dic[s[0]] = i
    else:
        dic[s[0:2]] = i

print(sorted(dic.items(),key=lambda x:x[1]))
