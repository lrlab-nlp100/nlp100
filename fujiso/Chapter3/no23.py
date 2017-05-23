# coding: utf-8
"""
自然言語処理100本ノック

23. セクション構造

記事中に含まれるセクション名と
そのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""

import re
from no20 import read_json


def get_section(article):
    pattern = re.compile(r"^=(=+)(.+?)(=+)=")

    for line in read_json().split("\n"):
        section = re.search(pattern, line)
        if section:
            print(
                "level{0}: {1}".format(
                    len(section.group(1)),
                    section.group(2)
                )
            )


if __name__ == '__main__':
    get_section(read_json())
