# -*- coding: utf-8 -*-
# #24. ファイル参照の抽出
# 記事から参照されているメディアファイルをすべて抜き出せ
import re
from pyknock20 import  extract_from_json

def extract_media_file(article):
    for string in article:
        matchs = re.search(r"(File:|ファイル:)(.*?)\|", string)
        if matchs is not None:
            print(matchs.group(2))

if __name__ == "__main__":
    extract_media_file(extract_from_json(u"イギリス").split("\n"))