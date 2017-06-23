#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．



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

        x_axis=[]
        y_axis=[]

        for i in fdist1.most_common():
            x_axis.append(i[0])
            y_axis.append(i[1])

        plt.bar(range(0, len(y_axis)),y_axis)
        plt.xticks(range(0, len(x_axis)),x_axis)
        plt.show()

print('done')