# coding: utf-8
"""
自然言語処理100本ノック

14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．


確認にはheadコマンドを用いよ．

確認コマンド:
head:ファイルの先頭からnum行だけ出力
head -[num] [file]

$ head -5 hightemp.txt
"""
from argument import argument


def show_nlines(filename, N):
    with open(filename) as f:
        for i, line in zip(range(N), f):
            print(line, end="")


if __name__ == '__main__':
    args = argument()
    show_nlines(args.filename, args.num)
