#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from nlp021 import UK

pattern = re.compile(r'^\[\[Category:(.*?)(?:\|.*)?\]\].*',re.MULTILINE)
#(.*?)キャプチャ対象(?:\|.*)非対称(?:\|.*)?

#findall文字列中でパターンにマッチしたもの返す
categories = pattern.findall(UK())

for category in categories:
    print(category)
