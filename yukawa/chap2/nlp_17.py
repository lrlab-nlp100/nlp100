# -*- encode: utf-8 -*-
with open('hightemp.txt','r') as f:
    l = []
    p = []
    for line in f:
        l = line.split()
        p.append(l[0]) 
    p = set(p)
    print(p)

# sort col1.txt | uniq
