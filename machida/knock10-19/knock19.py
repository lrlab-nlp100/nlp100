# -*- coding: utf-8 -*-
from collections import defaultdict

f = open('hightemp.txt')
txt = f.readlines()
f.close()
dic = defaultdict(int)
lit = list(map(lambda x:x.split('\t')[0], txt))

for l in lit:
    dic[l] += 1
for d in reversed(sorted(dic.items(), key=lambda x:x[1])):
    print(d[0])

# command
# cut -f1 hightemp.txt | sort | uniq -c | sort -r | cut -c 6-
