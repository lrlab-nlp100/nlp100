#! /usr/bin/env python

import re
from typing import List
from stemming.porter2 import stem
import pprint
import json
import corenlp


def main():
    with open("p50_sentence.txt", "r", encoding="utf-8") as f:
        s = f.readlines()
        with open("p53_parsed.txt", "w", encoding="utf-8") as w:

            # corenlp-python is only availabl in version 2013-06-20.
            parser = corenlp.StanfordCoreNLP(corenlp_path="./stanford-corenlp-full-2013-06-20/",
                                             properties="./user.properties")
            for line in s:
                result_json = json.loads(parser.parse(line))
                ws = result_json["sentences"][0]["words"]
                for word in map(lambda l: l[0], ws):
                    print(word)
                    w.write(word + "\n")


if __name__ == "__main__":
    main()
