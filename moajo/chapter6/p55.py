#! /usr/bin/env python

import re
from typing import List
from stemming.porter2 import stem
import pprint
import json
import corenlp
import re


# see http://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html
# list of tagging of part of speech
def main():
    with open("p54_tagged.txt", "r", encoding="utf-8") as f:
        s = f.readlines()

        # parser = corenlp.StanfordCoreNLP(corenlp_path="./stanford-corenlp-full-2013-06-20/")
        for line in s:
            if re.search("NNP$", line) is not None:
                print(line[:-1])  # last char is \n.


if __name__ == "__main__":
    main()
