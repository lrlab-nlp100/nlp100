# coding: utf-8
"""
自然言語処理100本ノック

19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる

各行の1列目の文字列の出現頻度を求め，
その高い順に並べて表示せよ．

確認にはcut, uniq, sortコマンドを用いよ．


確認コマンド:

$ cut -f 1 hightemp.txt | sort | uniq -c |sort -r
"""
from collections import Counter


def word_freqency(wordlist):
    cnt = Counter()
    for word in wordlist:
        cnt[word] += 1
    for w, n in cnt.most_common():
        print(w + "\t" + str(n))


if __name__ == '__main__':
    with open("col1.txt") as f:
        word_freqency(f.readlines())
