# -*- coding: utf-8 -*-
# 23. セクション構造
# 記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
import re
from pyknock20 import  extract_from_json

def section_and_level_collector(article):
    for string in article:
        matchs = re.search(r"^(=+)(.*?)(=+)$", string)
        if matchs is not None:
            print("section:" + matchs.group(2) + " level:" + str(len(matchs.group(1)) - 1))

if __name__ == "__main__":
    section_and_level_collector(extract_from_json(u"イギリス").split("\n"))


#print(matchs.group(0))
#print(matchs.group(1))
#print(matchs.group(2))
#print(matchs.group(3))
#==国名==
# ==
# 国名
# ==