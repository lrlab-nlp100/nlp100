#! /usr/bin/env python

import re
from typing import List


def main():
    with open("p50_sentence.txt", "r", encoding="utf-8") as f:
        s = f.readlines()
        with open("p51_word.txt", "w", encoding="utf-8") as w:
            for sentence in s:
                words = sentence.strip().split(" ")
                for word in words:
                    last_char = word[-1]
                    if last_char == "," or last_char == ".":
                        word = word[:-1]
                    w.write(word + "\n")
                w.write("\n")


if __name__ == "__main__":
    main()
