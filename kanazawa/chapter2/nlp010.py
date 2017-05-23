#!/usr/bin/env python
# -*- coding: utf-8 -*-

#行数をカウントせよ．確認にはwcコマンドを用いよ．

import sys

f = open(sys.argv[1])
#f = open('hightemp.txt')
lines = f.readlines()#１行ごとにリストとして読み込み
print(len(lines))#リストの長さ

f.close()

"""
wcコマンド

cat hightemp.txt | wc オプション
-l 行数
-m　文字数

wc higetemp.txt
行数　単語数　バイト数
"""
