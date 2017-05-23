#! /usr/bin/env python

from typing import List
import random


def ext_context(sent: List[str], index: int):
    range_ = random.randint(1, 5)
    return sent[max(0, index - range_):index], sent[index + 1:min(index + range_, len(sent)) + 1]


def main():
    with open("p81_replaced.txt", "r", encoding="utf-8")as text:
        with open("p82_context.txt", "w", encoding="utf-8") as w:
            for i, line in enumerate(text):
                print("{0}".format(i))
                spl = line.split()
                words = []
                for wd in spl:
                    ww = wd.strip()
                    if ww == "":
                        continue
                    words.append(ww)
                # words = list(filter(lambda s:s!="",map(lambda it:it.strip(),line.split())))
                for i in range(len(words)):
                    ctx = ext_context(words, i)
                    for c in ctx[0]:
                        w.write("{0}\t{1}\n".format(words[i], c))
                    for c in ctx[1]:
                        w.write("{0}\t{1}\n".format(words[i], c))


if __name__ == "__main__":
    main()
