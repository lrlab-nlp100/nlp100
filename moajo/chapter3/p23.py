#!/usr/bin/env python

import re
from p20 import read_eng


def get_cap_list(lines):
    regex = re.compile(r"=+([^=]+)=+")
    ret = []
    for l in lines:
        mat = regex.match(l)
        if mat is not None:
            ret.append((mat.group(1), l.find(mat.group(1))))
    return ret


def main():
    str_ = read_eng()
    for a in get_cap_list(str_.split("\\n")):
        print(a)


if __name__ == "__main__":
    main()
