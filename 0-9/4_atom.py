# 04. 元素記号

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

dic = {}
for i, atom in enumerate(str.split()):
    n = i + 1
    l = 1 if n in (1, 5, 6, 7, 8, 9, 15, 16, 19) else 2
    dic[atom[:l]] = n
print(sorted(dic.items(), key=lambda x: x[1]))
