#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

'''

import os
os.chdir('/Users/kokurin/PycharmProjects/python/100本/kokurin/Chapter4/')

import re
import nltk
import matplotlib.pyplot as plt

file_name='neko.txt.mecab'
neko_wordlist = []
point=0

def neko_words(line):

    l = re.split('\t',line)

    if l[0]=='\u3000':
        neko_wordlist.append(neko_wordlist[point-1])
    else:
        neko_wordlist.append(l[0])


if __name__ == '__main__':
    with open(file_name) as file:
        for line in file:
            if re.search("EOS", line):
                continue
            neko_words(line)
            point += 1
        fdist1 = nltk.FreqDist(neko_wordlist) #排序
        print(fdist1.most_common(10))

        x_axis=[]
        y_axis=[]

        for i in fdist1.most_common(10):
            x_axis.append(i[0])
            y_axis.append(i[1])

        plt.bar(range(0, 10),y_axis)
        plt.xticks(range(0, 10),x_axis)
        plt.show()
