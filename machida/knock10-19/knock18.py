# -*- coding: utf-8 -*-

f = open('hightemp.txt')
txt = f.readlines()
f.close()

lit = list(map(lambda x:x.split('\t'), txt))
sorted(lit[2])

for l in lit:
    print('\t'.join(l), end='')

# command
# sort -r -nk3 hightemp.txt
