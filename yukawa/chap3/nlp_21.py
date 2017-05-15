import re
with open('English.json','r') as f:
    for m in re.findall(r'\[\[Category:.*\]\]',''.join(f.readlines())):
        print(m)

