# coding: utf-8
"""
自然言語処理100本ノック

06. 集合

"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""
from no05 import ngram


def show_sets(x, y, n=2):
    x = set(ngram(x, n))
    y = set(ngram(y, n))
    print("和集合 x | y ={}".format(x | y))
    print("積集合 x & y ={}".format(x & y))
    print("差集合 x - y ={}".format(x - y))


if __name__ == "__main__":
    show_sets("paraparaparadise", "paragraph")
