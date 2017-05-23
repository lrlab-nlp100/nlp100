# coding: utf-8
"""
自然言語処理100本ノック

21. カテゴリ名を含む行を抽出

記事中でカテゴリ名を宣言している行を抽出せよ
"""

from no20 import read_json
import re


def get_category(article):
    out = list()
    pattern = re.compile("^\[\[Category:")
    for a in article.split('\n'):
        if re.match(pattern, a):
            print(a)
            out.append(a)
    return out


if __name__ == '__main__':
    get_category(read_json())
