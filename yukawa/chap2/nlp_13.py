# -*- coding: utf-8 -*-

with open('col1.txt','r') as col1,open('col2.txt','r') as col2,open('col12.txt','w') as col12:
    line2 = ""
    for line in col1:
        line2 = col2.readline()
        line = line[:-1]
        line += '\t'+line2
        col12.write(line)
# paste col1.txt col2.txt > col12.txt
