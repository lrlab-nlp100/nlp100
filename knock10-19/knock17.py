# -*- coding: utf-8 -*-

f = open('hightemp.txt', 'r')
txt = f.readlines()
f.close()

s = set()
txt = map(lambda x:x.split('\t')[0], txt)
for t in txt:
    s.add(t)

print(s)

# command
# cut -f1 hightemp.txt | sort | uniq
