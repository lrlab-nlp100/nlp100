#! /usr/bin/env python

import re
from typing import List


def spl_sentence(s: str) -> List[str]:
    s = re.sub(r"[\n ]+", " ", s).strip()
    space_index = s.find(" ")

    ret = []

    while space_index != -1:
        if s[space_index - 1] in [".", ";", ":", "?", "!"] and s[space_index + 1].isupper():
            ret.append(s[:space_index])
            s = s[space_index + 1:]
            space_index = s.find(" ")
        else:
            space_index = s.find(" ", space_index + 1)
    ret.append(s)
    return ret


def main():
    with open("nlp.txt", "r", encoding="utf-8") as f:
        s = f.read()
        spl = spl_sentence(s)
        with open("p50_sentence.txt", "w", encoding="utf-8") as w:
            for sentence in spl:
                w.write(sentence + "\n")


if __name__ == "__main__":
    main()
