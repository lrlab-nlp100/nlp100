# -*- coding: utf-8 -*- 

f = open('hightemp.txt','r')
col1 = open('col1.txt','w')
col2 = open('col2.txt','w')
for line in f:
    col_list = line.split()
    col1.write(col_list[0]+'\n')
    col2.write(col_list[1]+'\n')
f.close()
col1.close()
col2.close()
