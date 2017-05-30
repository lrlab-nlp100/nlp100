# -*- coding: utf-8 -*-
import sys

args = sys.argv
f = open('hightemp.txt', 'r')
txt = f.readlines()[::-1]
line = len(f.readlines())
f.close()
for i in reversed(range(int(args[1]))):
    print(txt[line + i], end='')

# command
# tail -3 hightemp.txt
