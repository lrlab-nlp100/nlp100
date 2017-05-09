# coding: utf-8
"""
自然言語処理100本ノック

17. １列目の文字列の異なり

1列目の文字列の種類（異なる文字列の集合）を求めよ．

確認にはsort, uniqコマンドを用いよ


$ cut -f1 hightemp.txt |sort | uniq
$ sort -t$'\t' -k1,1 hightemp.txt|cut -f1 | uniq
"""

from no12 import extract_col


def set_str(file="./out/col1.txt"):
    with open(file) as f:
        set_text = set(f.readlines())
    for i in range(len(set_text)):
        print(set_text.pop())


if __name__ == '__main__':
    extract_col(1)
    set_str()
