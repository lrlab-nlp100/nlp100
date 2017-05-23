import re
with open('English.txt','r',encoding='utf-8') as f:
    for m in re.findall(r'(?<=\[\[Category:)(.*)\]\]',''.join(f.readlines())):
        print(m)
