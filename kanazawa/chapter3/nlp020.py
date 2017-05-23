#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gzip
import json

with gzip.open("jawiki-country.json.gz", "rt") as f:
    article = f.readline()#1行ずつ読み込み
    while article:
        json_dict = json.loads(article)#load関数で読み込むと辞書型
        if json_dict['title'] == 'イギリス':
            print(json_dict['text'])
        article = f.readline()
