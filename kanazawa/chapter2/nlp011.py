#!/usr/bin/env python
# -*- coding: utf-8 -*-

#タブをスペースに置換
import sys
with open(sys.argv[1]) as f:
    lines = f.read()

print(lines.replace("\t", " "))

"""
expandコマンド：タブをスペースに変換
cat hightemp.txt |expand -t 4
-t　タブ幅指定（デフォルト８）
"""
