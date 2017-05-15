import re
from collections import Counter
with open('English.json','r') as f:
    for m in re.findall('=[=]+.*=[=]+',''.join(f.readlines())):
        c = Counter(m)
        print(m,int((c['=']/2)-1))
