#!/usr/bin/env python

import re
from p20 import read_eng


def get_category_lines(lines):
    regex = re.compile(r"\[\[Category:([^]]+)\]\]")
    return list(filter(lambda l: re.search(regex, l) is not None, lines))


def main():
    str_ = read_eng()
    for l in get_category_lines(str_.split("\\n")):
        print(l)


if __name__ == "__main__":
    main()
