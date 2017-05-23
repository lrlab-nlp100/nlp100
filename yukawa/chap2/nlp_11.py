# -*- coding: utf-8 -*-

with open('hightemp.txt',mode = 'r',encoding = 'utf-8') as f,open('new-hightemp.txt','w') as ret:
    ret.write(''.join(f.readlines()).replace('\t',' '))

# expand -t 1 hightemp.txt
