# -*- coding: utf-8 -*-
# 22. カテゴリ名の抽出
# 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
import re
from pyknock21 import extract_text_including_category
from pyknock20 import  extract_from_json

def extract_category(list):
    category_list = []
    for line in list:
        matchs = re.search(r"^\[\[Category:(.*?)(|\|.*?)\]\]", line)
        if matchs is not None:
            category_list.append(matchs.group(1))
            category2 = re.sub(re.compile("[!-/:-@[-`{-~]"), '', matchs.group(2))
            if category2 is not "":
                category_list.append(category2)
    return category_list


if __name__ == "__main__":
    print(extract_category(extract_text_including_category(extract_from_json(u"イギリス").split("\n"))))