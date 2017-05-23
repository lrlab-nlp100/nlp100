# coding: utf-8
"""
自然言語処理100本ノック

22. カテゴリ名の抽出

記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

from no20 import read_json
import re


def get_category_name(article):
    pattern = re.compile(r"^\[\[Category:(.+?)(\||\]\])")
    out = list()

    for line in article.split("\n"):
        category = re.search(pattern, line)
        if category:
            print(category.group(1))
            out.append(category.group(1))
    return out


if __name__ == '__main__':
    get_category_name(read_json())
