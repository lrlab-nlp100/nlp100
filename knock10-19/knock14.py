# -*- coding: utf-8 -*-
import sys

args = sys.argv
f = open('hightemp.txt', 'r')
txt = f.readlines()
f.close()
for i in range(int(args[1])):
    print(txt[i], end='')

# command
# head -3 hightemp.txt
