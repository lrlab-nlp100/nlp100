#! /usr/bin/env python

import re
from stemming.porter2 import stem
from chapter8.p71 import StopwordChecker
from typing import List
from pymongo import MongoClient

# client = MongoClient("localhost:27017")
# c = client["p64"]["artists"]


# 72. 素性抽出
# 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
# 素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．

def extract_feature(line: str, checker: StopwordChecker)->List[str]:
    words = re.compile(r'[,.:;\s]').split(line)
    return [stem(w) for w in words[1:] if w != "" and not checker.isStopword(w)]


def main():
    with open("p70_concat.txt", "r", encoding="ISO-8859-1")as f:
        lines = f.readlines()

    features = []
    checker = StopwordChecker()
    for line in lines:
        print("extracting... : " + line)
        features.append((line[:-1], extract_feature(line, checker)))

    with open("p72_feature.txt", "w", encoding="utf-8") as w:
        for feature in features:
            f = feature[1]
            w.write("{0}\t{1}\n".format(feature[0], " ".join(f)))


if __name__ == "__main__":
    main()
