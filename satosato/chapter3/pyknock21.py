# -*- coding: utf-8 -*-
# 21. カテゴリ名を含む行を抽出
# 記事中でカテゴリ名を宣言している行を抽出せよ．
from pyknock20 import extract_from_json

def extract_text_including_category(articles):
    list = []
    for article in articles:
        if "Category" in article:
            list.append(article)
    return list


if __name__ == "__main__":
    print(extract_text_including_category(extract_from_json(u"イギリス").split("\n")))