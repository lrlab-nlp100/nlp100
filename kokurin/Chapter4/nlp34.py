#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''

34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．

'''

import os
os.chdir('/Users/kokurin/PycharmProjects/python/100本/kokurin/Chapter4/')

import re
file_name='neko.txt.mecab'
nekolist = []
b=0

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

            if a['surface']=='の' and a['pos']=='助詞':
                x=nekolist[b - 1]['surface']
                y=nekolist[b + 1]['surface']
                print(x,y)
            b +=1