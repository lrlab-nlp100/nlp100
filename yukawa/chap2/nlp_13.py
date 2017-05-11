# -*- coding: utf-8 -*-

col1 = open('col1.txt','r')
col2 = open('col2.txt','r')
col12 = open('col12.txt','w')
line2 = ""
for line in col1:
    line2 = col2.readline()
    line = line[:len(line)-1]
    line += '\t'
    line += line2
    col12.write(line)

col1.close()
col2.close()
col12.close()

