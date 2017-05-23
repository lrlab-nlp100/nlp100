#! /usr/bin/env python
import sys

import re
from stemming.porter2 import stem

from chapter8.p71 import gen_stop_word_checker
from chapter8.class_logistic_regression import LogisticRegression


def main():
    with open("p72_feature.txt", "r", encoding="utf-8")as f:
        lines = f.readlines()

    lr = LogisticRegression()
    lr.restore_weights("p73_weights.txt")

    for line in lines:
        spl = line[:-1].split("\t")
        sentence = spl[0]
        features = spl[1].split(" ")
        p = lr.predict(features)

        print("p:{0}\t{2}@{1}".format(p, sentence, "+" if p > 0.5 else "-"))


if __name__ == "__main__":
    main()
