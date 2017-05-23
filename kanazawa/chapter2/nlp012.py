#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

with open(sys.argv[1]) as f, open ('col1.txt',"w") as c1, open ('col2.txt',"w") as c2:
    for line in f:
        col = line.split('\t')
        print(col)
        c1.write(col[0] + '\n')
        c2.write(col[1] + '\n')
