#!/usr/bin/env python
# -*- coding: utf-8 -*-
import gzip
import json
import re

def UK():
    with gzip.open("jawiki-country.json.gz", "rt") as f:
        for line in f:
            data = json.loads(line)
            if data['title'] == 'イギリス':
                return data['text']
    raise ValueError("error")#エラー

if __name__ == '__main__':#関数用

#re.MULYILINE対象データが複数行の時
    pattern = re.compile(r'(\[\[Category:.*\]\].*)',re.MULTILINE)

#findall文字列中でパターンにマッチしたもの返す
    categories = pattern.findall(UK())

    for category in categories:
        print(category)
