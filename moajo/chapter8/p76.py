#! /usr/bin/env python
import sys

import re
from stemming.porter2 import stem

from chapter8.p71 import gen_stop_word_checker
from chapter8.class_logistic_regression import LogisticRegression

def show_result(lines,lr):
    res = []
    for line in lines:
        spl = line[:-1].split("\t")
        sentence = spl[0]
        features = spl[1].split(" ")
        p = lr.predict(features)

        res.append("{0}\t{1}\t{2}".format(sentence[:2], "+1" if p > 0.5 else "-1", p))
    return res
def main():
    with open("p72_feature.txt", "r", encoding="utf-8")as f:
        lines = f.readlines()

    lr = LogisticRegression()
    lr.restore_weights("p73_weights.txt")

    with open("p76_result.txt", "w", encoding="utf-8") as w:
        for line in lines:
            spl = line[:-1].split("\t")
            sentence = spl[0]
            features = spl[1].split(" ")
            p = lr.predict(features)

            print("{0}\t{1}\t{2}".format(sentence[:2], "+1" if p > 0.5 else "-1", p))
            w.write("{0}\t{1}\t{2}\n".format(sentence[:2], "+1" if p > 0.5 else "-1", p))


if __name__ == "__main__":
    main()
