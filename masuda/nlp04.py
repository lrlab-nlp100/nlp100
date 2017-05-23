import re
str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
str = re.sub(r'[,.]', '', str)
words = str.split()
dic = {}
for i in range(len(words)):
    if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        dic.update({words[i][0]: i+1})
    else:
        dic.update({words[i][:2]: i+1})
print(dic)
