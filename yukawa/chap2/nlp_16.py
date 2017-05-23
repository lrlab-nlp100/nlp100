# -*- coding: utf-8 -*-
import sys
arg = sys.argv
n = int(arg[1])
name = arg[2]
cnt = sum(1 for i in open(name))
n = round(cnt/n)
nfile,nline = 0,0
with open(name,'r') as f:
    for line in f:
        if nline == 0:
            f1 = open(name[:-4]+str(nfile)+'.txt','w')
            f1.write(line)
            nfile += 1
            nline += 1
        elif nline < n-1:
            f1.write(line)
            nline += 1
        elif nline == n-1:
            f1.write(line)
            f1.close()
            nline = 0
f1.close()

# split -l $(expr $(cat hightemp.txt | wc -l) / N) hightemp.txt
