# -*- coding: utf-8 -*-
import sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

f = open('hightemp.txt')
line = len(f.readlines())
print(line)
f.close()
