#!/usr/bin/env python

import re
from p20 import read_eng
from p21 import get_category_lines


def main():
    str_ = read_eng()
    regex = re.compile(r"\[\[Category:([^\]]+)\]\]")
    for l in get_category_lines(str_.split("\\n")):
        print(regex.match(l).group(1))


if __name__ == "__main__":
    main()
