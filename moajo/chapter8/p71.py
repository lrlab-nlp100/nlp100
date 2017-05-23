#! /usr/bin/env python
import sys


def gen_stop_word_checker():
    with open("p71_stopword.txt", "r", encoding="utf-8") as f:
        stops = f.readlines()

    return lambda w: w in map(lambda s: s[:-1], stops)


def check_stop_word(word):
    with open("p71_stopword.txt", "r", encoding="utf-8") as f:
        stops = f.readlines()

    return word in map(lambda s: s[:-1], stops)


def main():
    arg = sys.argv[1]

    print(check_stop_word(arg))


if __name__ == "__main__":
    main()
