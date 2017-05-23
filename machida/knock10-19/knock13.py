# -*- coding: utf-8 -*-

col1 = open('col1.txt', 'r')
col2 = open('col2.txt', 'r')
f = open('merge.txt', 'w')
for (c1, c2) in zip(col1, col2):
    f.write(c1.strip() + '\t' +c2.strip() + '\n')

col1.close()
col2.close()
f.close()

# command
# paste col1.txt col2.txt > merge_c.txt
