#!/usr/bin/env python


import random
from p03 import spl_word


def word_09(s):
    if len(s) < 5:
        return s
    l = list(s[1:-1])
    random.shuffle(l)
    return s[0] + "".join(l) + s[-1]


def f_09(s):
    mapped = map(lambda ss: word_09(ss), spl_word(s))
    return " ".join(mapped)


def main():
    s = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(f_09(s))


if __name__ == "__main__":
    main()
