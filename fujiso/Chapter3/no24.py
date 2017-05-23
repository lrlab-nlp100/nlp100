# coding: utf-8
"""
自然言語処理100本ノック

24. ファイル参照の抽出

記事から参照されているメディアファイルをすべて抜き出せ
"""

from no20 import read_json
import re


def get_reference(article):
    pattern = re.compile(r"(File|ファイル):(.+?)\|")

    for line in article.split("\n"):
        ref = re.search(pattern, line)
        if ref:
            print(ref.group(2))


if __name__ == '__main__':
    get_reference(read_json())
