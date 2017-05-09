# -*- coding: utf-8 -*-

f = open("hightemp.txt",'r')
cnt = 0
for line in f:
    cnt += 1
print(cnt)
f.close()

# wc -l hightemp.txt 
