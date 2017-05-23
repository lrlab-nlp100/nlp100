#! /usr/bin/env python
import sys

import re
from stemming.porter2 import stem

from chapter8.p71 import gen_stop_word_checker


def extract_feature(line, checker):
    words = re.compile(r'[,.:;\s]').split(line)
    # v = words[0]

    f = []
    for word in words[1:]:
        if word != "" and not checker(word):
            f.append(stem(word))
    return f


def main():
    checker = gen_stop_word_checker()
    with open("p70_concat.txt", "r", encoding="ISO-8859-1")as f:
        lines = f.readlines()

    features = []
    for line in lines:
        print("extracting... : " + line)
        features.append((line[:-1], extract_feature(line, checker)))

    # print(features)

    with open("p72_feature.txt", "w", encoding="utf-8") as w:
        for feature in features:
            f = feature[1]
            w.write("{0}\t{1}\n".format(feature[0], " ".join(f)))


if __name__ == "__main__":
    main()
