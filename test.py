# coding: utf-8
import os
os.chdir('/Users/kokurin/PycharmProjects/python/100本/Chapter2')

fname = 'hightemp.txt'
lines = open(fname).readlines()
lines.sort(key=lambda line: float(line.split('\t')[2]), reverse=True)

for line in lines:
    print(line, end='')