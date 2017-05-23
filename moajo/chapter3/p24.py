#!/usr/bin/env python

import re
from p20 import read_eng


def main():
    str_ = read_eng()
    regex = re.compile(r"\[\[ *(?:File|ファイル):(.*?)\|")
    for l in str_.split("\\n"):
        match = regex.search(l)
        if match is not None:
            print(match.group(1))


if __name__ == "__main__":
    main()
