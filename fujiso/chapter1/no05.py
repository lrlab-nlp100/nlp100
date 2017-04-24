# coding: utf-8
"""
自然言語処理100本ノック

05. n-gram

与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""


def ngram(x, n):
    out = []
    num = len(x) - n + 1  # ワード数の計算
    for i in range(num):
        out.append(x[i:i + n])
    return out


if __name__ == "__main__":
    given_sent = "I am an NLPer"
    given_words = given_sent.split()
    print(ngram(given_sent, 2))
    print(ngram(given_words, 2))
