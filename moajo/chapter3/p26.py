#!/usr/bin/env python

import re
from p20 import read_eng
from common import get_brace


def main():
    str_ = read_eng()
    pos = str_.find("{{基礎情報")
    content = get_brace(str_, pos, "{{", "}}")[:-2]
    regex = re.compile(r"(.+?)=(.+)")
    obj = {}
    for s in content.split("\\n|")[1:]:
        match = regex.match(s)
        sub = re.sub(r"'{2,5}(.*?)'{2,5}", r"\1", match.group(2))
        obj[match.group(1)] = sub
    print(obj)


if __name__ == "__main__":
    main()
