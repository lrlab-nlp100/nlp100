# coding: utf-8
"""
自然言語処理100本ノック

15. 末尾のN行を出力

自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．

確認にはtailコマンドを用いよ．

確認コマンド:
tail:ファイルの末尾からnum行だけ出力
tail -[num] hightemp.txt

$ tail -5 hightemp.txt
"""
from argument import argument


def end_nlines(filename, N):
    with open(filename) as f:
        lines = f.readlines()
    for line in lines[-N:]:
        print(line, end="")


if __name__ == '__main__':
    args = argument()
    end_nlines(args.filename, args.num)
