#! /usr/bin/env python

import re
from typing import List
from stemming.porter2 import stem


def main():
    a = stem("Many challenges in NLP")
    print(a)

    with open("p51_word.txt", "r", encoding="utf-8") as f:
        s = f.readlines()
        with open("p52_stem.txt", "w", encoding="utf-8") as w:
            for word in s:
                word = word.strip()
                if word != "":
                    w.write("{0}\t{1}\n".format(word, stem(word)))


if __name__ == "__main__":
    main()
