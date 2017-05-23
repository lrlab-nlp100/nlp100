import re
with open('English.txt','r') as f:
    for m in re.findall(r'\[\[Category:.*\]\]',''.join(f.readlines())):
        print(m)

