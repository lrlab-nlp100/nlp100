#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

33. サ変名詞
サ変接続の名詞をすべて抽出せよ．

'''

import os
os.chdir('/Users/kokurin/PycharmProjects/python/100本/kokurin/Chapter4/')

import re
file_name='neko.txt.mecab'
nekolist = []
from nlp30 import mapper_neko

if __name__ == '__main__':
    point = 0
    with open(file_name) as file:
        for line in file:
            if re.search("EOS", line):
                continue
            nekolist.append(mapper_neko(line,nekolist,point))
            point += 1

        for a in nekolist:
            if a['pos']=='名詞' and a['pos1']=='サ変接続':
                print(a['surface'])