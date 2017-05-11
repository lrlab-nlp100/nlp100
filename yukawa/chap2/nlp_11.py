# -*- coding: utf-8 -*-

with open('hightemp.txt',mode = 'r',encoding = 'utf-8') as f:
    with open('new-hightemp.txt','w') as ret:
        for line in f:
            s = line.replace('\t',' ')
            ret.write(s)
    ret.close()
f.close()
