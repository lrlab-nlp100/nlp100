#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
31. 動詞
動詞の表層形をすべて抽出せよ．

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
            if a['pos' or 'pos1']=='動詞':
                print(a['surface'])