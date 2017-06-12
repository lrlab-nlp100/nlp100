#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）を
キーとするマッピング型に格納し，1文を形態素（マッピング型）のリストとして表現せよ．
第4章の残りの問題では，ここで作ったプログラムを活用せよ．

'''

import os
os.chdir('/Users/kokurin/PycharmProjects/python/100本/kokurin/Chapter4/')

import re
file_name='neko.txt.mecab'
nekolist = []


def mapper_neko(line,nekolist,point):
    nekomap = {}

    l = re.sub(r"\t", ",",line,count=1)
    l = re.split(',',l)

    if l[0]=='\u3000':
        nekomap['surface'] = nekolist[point - 1]['surface']
    else:
        nekomap['surface'] = l[0]

    nekomap['base'] = l[7]
    nekomap['pos'] = l[1]
    nekomap['pos1'] = l[2]

    return nekomap

if __name__ == '__main__':
    point = 0
    with open(file_name) as file:
        for line in file:
            if re.search("EOS", line):
                continue
            nekolist.append(mapper_neko(line,nekolist,point))
            point += 1

print(nekolist)