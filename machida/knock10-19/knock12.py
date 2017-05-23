# -*- coding: utf-8 -*-

f = open('hightemp.txt')
txt = f.readlines()
f.close()
col1 = open('col1.txt', 'w')
col2 = open('col2.txt', 'w')

for t in txt:
    lit = t.split('\t')
    col1.write(lit[0] + '\n')
    col2.write(lit[1] + '\n')

col1.close()
col2.close()

# command
# cut -f1 hightemp.txt > col1_c.txt
# cut -f2 hightemp.txt > col2_c.txt
