# -*- coding: utf-8 -*-
from stemming.porter2 import stem
import sys
txt = []
for line in sys.stdin:
    txt.append(str(line))
for line in txt:
    print(line[:-1]+'\t'+stem(line[:-1]))
