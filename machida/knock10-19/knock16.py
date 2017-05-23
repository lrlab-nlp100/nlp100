# -*- coding: utf-8 -*-
import sys, os

args = sys.argv
f = open('hightemp.txt', 'r')
txt = f.readlines()
former = int(len(txt) / int(args[1])) + 1
f.close()

os.chdir("./output")
try:
    for i in range(int(args[1])):
        with open("output" + str(i) + ".txt", 'w') as f:
            for j in range(former):
                f.write(txt[i * former + j])
except IndexError:
    pass

# command
# split -l 5 hightemp.txt output_c
