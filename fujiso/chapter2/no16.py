# coding: utf-8
"""
自然言語処理100本ノック

16. ファイルをN分割する

自然数Nをコマンドライン引数などの手段で受け取り，
入力のファイルを行単位でN分割せよ．

同様の処理をsplitコマンドで実現せよ．

確認コマンド:
$ split -l 8 hightemp.txt split
$ cat splitxa.txt
"""
from argument import argument


def splitlines(filename, N):
    with open(filename, 'r') as f:
        lines = f.readlines()
    line = len(lines) // N
    size = (line + 1 if (x < len(lines) % N) else line for x in range(N))
    total = 0
    for i, s in enumerate(size):
        with open("./out/split{}.txt".format(i), "w") as o:
            o.write("".join(lines[total:total + s]))
        total += s


if __name__ == '__main__':
    args = argument()
    splitlines(args.filename, args.num)
