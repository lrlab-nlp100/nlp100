# -*- coding: utf-8 -*- 

with open('hightemp.txt','r') as f,open('col1.txt','w') as col1,open('col2.txt','w') as col2:
    for line in f:
        col_list = line.split()
        col1.write(col_list[0]+'\n')
        col2.write(col_list[1]+'\n')

# cut -f1 hightemp.txt > col1.txt
# cut -f2 hightemp.txt > col2.txt
