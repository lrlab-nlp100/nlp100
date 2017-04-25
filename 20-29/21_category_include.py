# coding: UTF-8
# 21. カテゴリ名を含む行を抽出

from extract_from_json import extract_from_json

text = extract_from_json(u'イギリス').split("\n")

for i, line in enumerate(text):
    if line.find('[[Category') >= 0:
        print str(i + 1) + u'行'
